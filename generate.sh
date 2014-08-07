#!/bin/bash

rm -f result/all_metrics.py basic_metrics.py
python transform.py raw_html/cpu_metrics.html cpu >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/datastore_metrics.html datastore >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/disk_metrics.html disk >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/hbr_metrics.html hbr >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/managementAgent_metrics.html managementAgent >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/memory_metrics.html mem >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/network_metrics.html network >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/power_metrics.html power >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/rescpu_metrics.html rescpu >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/storageAdapter_metrics.html storageAdapter >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/storagePath_metrics.html storagePath >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/system_metrics.html system >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py
python transform.py raw_html/virtualDisk_metrics.html virtualDisk >> result/all_metrics.py
echo -ne '\n\n' >> result/all_metrics.py

cat >> result/all_metrics.py <<-EOF
ALL_METRICS = CPU_METRICS + DATASTORE_METRICS + DISK_METRICS + \\
    HBR_METRICS + MANAGEMENTAGENT_METRICS + MEM_METRICS + NETWORK_METRICS + \\
    POWER_METRICS + RESCPU_METRICS + STORAGEADAPTER_METRICS + \\
    STORAGEPATH_METRICS + VIRTUALDISK_METRICS
EOF

python transform_basic.py
