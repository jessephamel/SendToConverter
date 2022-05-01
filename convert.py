import ffmpeg
import os
import sys

def main(*args):
	dest_format = input("destination format: ")
	cwd = os.path.split(args[0][0])[0]

	try:
		os.makedirs(f'{cwd}/converted')
	except FileExistsError:
		print('converted folder exists')

	for f in args[0]:
		orig_name = os.path.split(f)[1].split('.')[0]
		new_name = f'{orig_name}.{dest_format}'	
			
		stream = ffmpeg.input(f)
		stream = ffmpeg.output(stream, f'{cwd}\\converted\\{new_name}')
		ffmpeg.run(stream)

if __name__ == "__main__":
	main(sys.argv[1:])