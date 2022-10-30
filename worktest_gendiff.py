from gendiff import generate_diff


diff = generate_diff(
    '/home/ovechka/test_dir/python-project-50/file1.json',
    '/home/ovechka/test_dir/python-project-50/file2.json'
    )
print(diff)
