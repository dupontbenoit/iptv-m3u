import re
import sys
import argparse

keywords = {}


class M3UFile:

    def __init__(self, file):
        self.file = file

    """
    Extract group-title
    """
    def extract_group_from_string(self, string):
        #print(string)
        return re.search('group-title="(.*)"', string).group(1)

    """
    List group titles
    """
    def groups(self):
        group_set = set()
        with open(self.file, "r", encoding="utf8") as f:
            for line in f:
                if line.startswith("#EXTINF:"):
                    group_name = self.extract_group_from_string(line)
                    group_set.add(group_name)
        return sorted(group_set)

    """
    Restrict list to channels with filter keywords
    """
    def filter(self, filters):
        results = []
        keep_next_row = False
        with open(self.file, "r", encoding="utf8") as f:
            # file header
            results.append(f.readline())
            for line in f:
                if keep_next_row:
                    results.append(line)
                    keep_next_row = False

                if any(keyword in line for keyword in filters):
                    results.append(line)
                    keep_next_row = True
        return results


"""
Load filters file
"""
def init_filters(filter_file):
    with open(filter_file, "r", encoding="utf8") as filters_file:
        keywords = filters_file.readlines()
    return keywords


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('--input', type=str,
                    help='Original M3U file')
    parser.add_argument('--output', type=str,
                    help='Resulting filtered M3U file')
    parser.add_argument('--filters', type=str,
                    help='Filter (txt) file containaing keywords to filter and keep. One keyword by line.')
    parser.add_argument('--list_groups', action="store_true",
                    help='List groups/categories from the M3U file')
    args = parser.parse_args()
    if args.input:
        m3u = M3UFile(args.input)
        if args.list_groups:
            for line in m3u.groups():
                print(line)
        if args.input and args.output and args.filters:
            keywords = init_filters(args.filters)
            with open(args.output, "w", encoding="utf8") as output:
                for line in m3u.filter(keywords):
                    print(line)
                    output.write(line)
    else:
        parser.error('You need to pass at least the input file')
