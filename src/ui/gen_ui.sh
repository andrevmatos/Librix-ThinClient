#!/bin/bash -x

for i in *.ui; do
    pyuic4 --from-imports -i 0 "$i" -o "$(echo $i | sed 's|.ui$|.py|g')"
done
exit 0
