#!/usr/bin/env python3
import sys

def main():
    print("--------------------------------------------------")
    print("  Kobi Text Editor v1.0.0 (Canerix CORE Ecosystem)")
    print("  Developed by Poniek Labs (labs.poniek.ca)")
    print("--------------------------------------------------")
    if len(sys.argv) > 1:
        print(f"Opening file: {sys.argv[1]}")
    else:
        print("No file specified. Running in interactive stub mode.")

if __name__ == "__main__":
    main()
