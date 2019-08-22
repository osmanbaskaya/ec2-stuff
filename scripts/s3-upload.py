import boto3
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--bucket', default='osmanbaskaya')
parser.add_argument('--s3-path', required=True)

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--directory', default=None)
group.add_argument('--file', default=None)

args = parser.parse_args()
print(args)

directory = args.directory
bucket = args.bucket
s3_path = args.s3_path

s3 = boto3.client('s3')

if directory is not None:
    for fn in os.listdir(args.directory):
        input_fn = os.path.join(directory, fn)
        output_fn = os.path.join(s3_path, os.path.basename(fn))
        print(f'Uploading {input_fn} to {output_fn}')
        s3.upload_file(input_fn, bucket, output_fn)
else:
    input_fn = os.path.join('.', args.file)
    output_fn = os.path.join(s3_path, os.path.basename(args.file))
    print(f'Uploading {input_fn} to {output_fn}')
    s3.upload_file(input_fn, bucket, output_fn)
