read Y M D;T=$(date --date="$Y-$M-$D" +%s); 
if [ $T -ge 600188400 ] && [ $T -le 1556550000 ]; then
    echo "YES"
else
    echo "NO"
fi
