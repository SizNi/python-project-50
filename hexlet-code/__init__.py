import argparse


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(prog = 'gendiff', description = description)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

if __name__ == '__main__':
    main()