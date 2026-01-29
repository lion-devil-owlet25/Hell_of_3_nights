def bitwise_demonstration():
	num = 10  # Binary: 1010
	
	# Left Shift: 10 * (2^2) = 40
	left_shifted = num << 2
	
	# Right Shift: 10 // (2^1) = 5
	right_shifted = num >> 1
	
	print(f"Original: {num} (Binary: {bin(num)})")
	print(f"Left Shift by 2: {left_shifted} (Binary: {bin(left_shifted)})")
	print(f"Right Shift by 1: {right_shifted} (Binary: {bin(right_shifted)})")

if __name__ == "__main__":
	bitwise_demonstration()
