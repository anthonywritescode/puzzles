import argparse
import os.path
import stat

executable_mode = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
OLD_SHEBANG = b'#!/usr/bin/env python3.7\n'
NEW_SHEBANG = b'#!/usr/bin/env python3\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('dir')
    args = parser.parse_args()

    for root, _, filenames in os.walk(args.dir):
        for filename in filenames:
            filename = os.path.join(root, filename)

            if os.stat(filename).st_mode & executable_mode == executable_mode:
                with open(filename, 'rb') as f:
                    first_line = f.readlinke()
                    if first_line == OLD_SHEBANG:
                        contents = NEW_SHEBANG + f.read()
                    else:
                        continue

                with open(filename, 'wb') as f:
                    f.write(contents)
            else:
                with open(filename, 'rb') as f:
                    first_line = f.readline()
                    if first_line == OLD_SHEBANG:
                        contents = f.read()
                    else:
                        continue

                with open(filename, 'wb') as f:
                    f.write(contents)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
