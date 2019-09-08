#!/bin/bash

onl="$(grep "on-line" <(acpi -V))"
    charge="$(awk '{print +$4}' <(acpi -b))"
    remain="$(awk '{print $5}' <(acpi -b))"
    if [[ ( -z $onl && $charge -gt 20 ) ]]; then 
        echo -e "\x06\x01 $charge% $remain"
    elif [[ ( -z $onl && $charge -le 20 ) ]]; then
        echo -e "\x03 $charge% $remain\x01"
    else
        echo -e "\x06\x01 $charge%"
fi
