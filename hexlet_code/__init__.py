import argparse
from gendiff import generate_diff


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(prog='gendiff', description=description)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == '__main__':
    main()
