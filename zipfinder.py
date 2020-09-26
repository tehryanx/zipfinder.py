#!/usr/bin/env python3

import fileinput

all_paths = []
all_filenames = []

extensions = [ "tar", "tar.gz", "tar.bz2", "tar.Z",
	"tar.xz", "tar.lz", "tar.lzma", "tbz2", "tlz",
	"txz", "gz", "bz2", "lz", "lzma", "z", "Z", "7z",
	"s7z", "dmg", "rar", "zip", "backup", "bak", "swp"
	]

extensions = [ "zip", "tar", "gz", "gzip", "bz2", "tar.gz", "tar.bz2", 
		"rar", "backup", "bak", "old", "7z" ]

def parse_paths(line):
	paths = []
	full_path = ""
	if len(line) > 0:
		if "//" in line: # remove protocol://
			line = "/".join(line.split("/")[3:])
		if len(line) > 0 and "?" in line: # remove any parameters
			line = line.split("?")[0]
		if len(line) > 0 and line[-1] == "/": #remove trailing slash
			line = line[:-1]
		for item in line.split("/"): # add each path depth as its own item to paths
			full_path = full_path + "/" + item # assemble full_path one directory at a time
			paths.append(full_path); # add it to the the list
		return paths
		
def generate_filenames(path):
	filenames = []
	for ext in extensions:
		filenames.append(path + "." + ext)
		if "." in path:
			filename_noext = path.split(".")[0] + "." + ext
			filenames.append(filename_noext)
		if "." not in path:
			repeat_last_dir = path.split("/")[-1]
			filenames.append(path + "/" + repeat_last_dir + "." + ext)
	return filenames

if fileinput.input():
	for line in fileinput.input():
		paths = parse_paths(line.strip())
		if paths:
			for path in paths:
				all_paths.append(path)

	uniq_paths = set(all_paths)

if uniq_paths:
	for path in uniq_paths:
		filenames = generate_filenames(path)
		if filenames: 
			for filename in filenames:
				all_filenames.append(filename)

	uniq_filenames = set(all_filenames)

if uniq_filenames:
	for item in uniq_filenames:
		print(item[1:])

