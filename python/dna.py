def dna(seq):
	print("Region name: " + seq[0])
	print("Nucleotides: " + seq[1].upper())
	print("Nuc. Counts: " + str(get_nucleotides_count(seq[1].upper())))
	print("Total Mass%: " + str(calculate_mass_percentage(seq[1])) + " of " + str(calculate_total_mass(seq[1])))
	print("Codons List: " + str(get_codons(seq[1])))
	if is_protein(seq[1]):
		print("Is Protein?: YES")
	else:
		print("Is Protein?: NO")



def get_nucleotides_count(str):
	lst = []
	lst.append(str.count("A"))
	lst.append(str.count("C"))
	lst.append(str.count("G"))
	lst.append(str.count("T"))
	return lst

def calculate_total_mass(str):
	lst = get_nucleotides_count(str.upper())
	return round((lst[0] * 135.128) + (lst[1] * 111.103) + (lst[2] * 151.128) + (lst[3] * 125.107) + (str.count("-") * 100.0), 1)

def calculate_mass_percentage(str):
	total = calculate_total_mass(str)
	lst = get_nucleotides_count(str.upper())
	ans = []
	ans.append(round(((lst[0]*135.128) / total) * 100, 1))
	ans.append(round(((lst[1]*111.103) / total) * 100, 1))
	ans.append(round(((lst[2]*151.128) / total) * 100, 1))
	ans.append(round(((lst[3]*125.107) / total) * 100, 1))
	return ans

def get_codons(str):
	lst = list(str.upper())
	the_max = lst.count("-")
	for x in range(0, the_max):
		lst.remove("-")
	without_junk = "".join(lst)
	ans = []
	for y in range(0, len(without_junk), 3):
		ans.append(without_junk[y:y+3])
	return ans

def is_protein(str):
	codons = get_codons(str)
	valid_stop_codons = ["TAA", "TAG", "TGA"]
	mass_percentages = calculate_mass_percentage(str)
	if codons[0] != "ATG" or valid_stop_codons.count(codons[len(codons) - 1]) == 0:
		return False
	elif len(codons) < 5:
		return False
	elif mass_percentages[1] + mass_percentages[2] < 30:
		return False
	return True

def main():
	dna(('cure for cancer protein', 'ATGCCACTATGGTAG'))
	dna(('captain picard hair growth protein', 'ATgCCAACATGgATGCCcGATAtGGATTgA'))
	dna(('bogus protein', 'CCATt-AATgATCa-CAGTt'))

main()

