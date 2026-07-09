#!/usr/bin/env bash
# Incomplete Script
# still in progress

#---WHAT THIS SCRIPT DOES---#
#This script is an automated setup utility that prepares your Raspberry Pi to run an RGB LED Matrix. 
#It forces strict error checking, automatically installs required system and Python dependencies, 
#locates and compiles the necessary hardware-level C++ drivers into Python modules,
#and permanently disables the Pi's onboard audio system to prevent sound card signals from causing the LED display to flicker.
#---------------------------#

#=========TO DO=========#
currently this script only validates and installs dependancies , add commands to run the actual python files needed to start the program and the matrix
#=======================#

set -euo pipefail

log() {
    printf '[startUp] %s\n' "$1"
}

need_apt_package() {
    dpkg -s "$1" >/dev/null 2>&1
}

python_has_module() {
    python3 - <<'PY' "$1"
import importlib.util
import sys

module_name = sys.argv[1]
raise SystemExit(0 if importlib.util.find_spec(module_name) else 1)
PY
}

install_apt_packages() {
    local packages_to_install=()
    local package

    for package in "$@"; do
        if ! need_apt_package "$package"; then
            packages_to_install+=("$package")
        fi
    done

    if ((${#packages_to_install[@]} > 0)); then
        log "Installing missing apt packages: ${packages_to_install[*]}"
        sudo apt-get update
        sudo apt-get install -y "${packages_to_install[@]}"
    else
        log "All required apt packages are already installed."
    fi
}

find_rgbmatrix_repo() {
    local candidate
    local candidates=(
        "${RPI_RGB_LED_MATRIX_PATH:-}" #this will be empty if the variable is not set, where do i set it?- 
        "$HOME/Desktop/rpi-rgb-led-matrix"
        "$HOME/rpi-rgb-led-matrix"
        "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../rpi-rgb-led-matrix"
    )

    for candidate in "${candidates[@]}"; do
        if [[ -n "$candidate" && -d "$candidate" && -f "$candidate/Makefile" ]]; then
            printf '%s\n' "$candidate"
            return 0
        fi
    done

    return 1
}

ensure_rgbmatrix_bindings() {
    if python_has_module rgbmatrix; then
        log "rgbmatrix Python module is already available."
        return 0
    fi

    log "rgbmatrix Python module is missing. Trying to build and install it from source."

    local repo_path
    if ! repo_path="$(find_rgbmatrix_repo)"; then
        log "Could not find the rpi-rgb-led-matrix repo. Set RPI_RGB_LED_MATRIX_PATH or clone it next to this project."
        exit 1
    fi

    pushd "$repo_path" >/dev/null
    make build-python PYTHON=python3
    sudo make install-python PYTHON=python3
    popd >/dev/null
}

ensure_sound_disabled() {
    local blacklist_file="/etc/modprobe.d/blacklist-rgb-matrix.conf"
    local blacklist_line="blacklist snd_bcm2835"
    local needs_update=0

    if [[ ! -f "$blacklist_file" ]] || ! grep -qxF "$blacklist_line" "$blacklist_file"; then
        log "Writing sound blacklist to $blacklist_file"
        printf '%s\n' "$blacklist_line" | sudo tee "$blacklist_file" >/dev/null
        needs_update=1
    else
        log "Sound blacklist already present."
    fi

    if ((needs_update)); then
        sudo update-initramfs -u
    fi

    if lsmod | grep -q '^snd_bcm2835'; then
        log "snd_bcm2835 is currently loaded. Reboot is required for the blacklist to take effect."
    fi
}

main() {
    local required_packages=(
        cython3
        python3-dev
        python3-tk
        python3-pil
    )

    install_apt_packages "${required_packages[@]}"
    ensure_rgbmatrix_bindings
    ensure_sound_disabled

    log "Startup checks complete."
}

main "$@"
#example
# 1. Force the script to jump to the directory where this .sh file lives
cd "$(dirname "$0")" || exit 1
####python3 PROGRAM_PYTHON_FILE_HERE
