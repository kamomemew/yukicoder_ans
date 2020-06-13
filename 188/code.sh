echo -E "$(for i in $(seq 1 365);do date -d "2016-01-01 $i days ago" '+%F'; done)"|sed -E "s@2015-([0-9][0-9])-([0-9])([0-9])@\1 \2 \3@g" | awk '$1 == $2+$3 { print }'|wc -l


