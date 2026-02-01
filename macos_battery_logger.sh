#!/bin/zsh

export LC_NUMERIC=C
LOG_FILE="battery_metrics.csv"

if [ ! -f "$LOG_FILE" ]; then
    echo "Timestamp,Voltage(V),Current(A),Power(W)" > "$LOG_FILE"
fi

echo "Battery monitoring started. Saving to $LOG_FILE (Ctrl+C to stop)"

while true; do
    ts=$(date "+%Y-%m-%d %H:%M:%S")

    read volt amp watt <<< $(ioreg -r -c AppleSmartBattery | awk '
        /"Voltage" =/ { v=$3/1000 }
        /"InstantAmperage" =/ { 
            a=$3
            if (a > 18000000000000000000) a -= 18446744073709551616
            a /= 1000 
        }
        END { printf "%.3f %.3f %.3f", v, a, v*a }
    ')

    echo "$ts,$volt,$amp,$watt" >> "$LOG_FILE"
    
    printf "\r[%s] Voltage: %6.3fV | Current: %6.3fA | Power: %6.3fW" "$ts" "$volt" "$amp" "$watt"
    
    sleep 1
done