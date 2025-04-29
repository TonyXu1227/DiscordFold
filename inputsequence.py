
import os
import time
from dotenv import load_dotenv
load_dotenv()
sequence = os.getenv('SEQUENCE')
f = open("input.fasta", "w")
f.write(">protein_monomer ")
f.write(sequence)
f.close()

try:
  os.system("rm -rf output")
  print("Old output file deleted")
except Exception as e:
  print(f"An error occurred: {e}")

try:
  os.mkdir("output")
  print("Output file created")
except FileExistsError:
  print("Output already exists")
except FileNotFoundError:
  print("Path not found.")
except Exception as e:
  print(f"An error occurred: {e}")

os.system("colabfold_batch --num-recycle 1 --num-models 1 input.fasta output/")
os.system("zip -r out.zip output")

print("Finished folding")