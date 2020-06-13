read  n m
for i in $(seq $n);do
    read l
    echo $l|grep -q "LOVE" && { echo YES;exit; }
done
echo NO
