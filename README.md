# IPTV M3U channels filter

Filter a big IPTV M3U file to smaller one with only the type of channels you need.

```bash
sample usage : iptv_channels.py --input original.m3u --output filtered.m3u --filters iptv_filters.txt
```

```bash
usage: iptv_channels.py [-h] [--input INPUT] [--output OUTPUT]
                        [--filters FILTERS] [--list_groups]

Optional app description

optional arguments:
  -h, --help         show this help message and exit
  --input INPUT      Original M3U file
  --output OUTPUT    Resulting filtered M3U file
  --filters FILTERS  Filter (txt) file containaing keywords to filter and
                     keep. One keyword by line.
  --list_groups      List groups/categories from the M3U file
```