'''
Python >> 07 July 2025
ระดับความยาก:  🌕🌕🌕🌗🌑🌑🌑🌑🌑🌑

เขียนฟังก์ชัน Python ชื่อ categorize_numbers(numbers) ที่รับลิสต์ของจำนวนเต็ม numbers เป็นอินพุต ฟังก์ชันควรคืนค่าเป็น Dictionary โดยมีคีย์สองคีย์:
'even': คีย์นี้ควรมีค่าเป็นลิสต์ของจำนวนคู่ทั้งหมดจาก numbers
'odd': คีย์นี้ควรมีค่าเป็นลิสต์ของจำนวนคี่ทั้งหมดจาก numbers

จำนวนในลิสต์ผลลัพธ์ควรคงลำดับเดิมไว้ตามที่ปรากฏในลิสต์อินพุต

ตัวอย่าง:
categorize_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
คืนค่า: {'even': [2, 4, 6, 8, 10], 'odd': [1, 3, 5, 7, 9]}

categorize_numbers([])
คืนค่า: {'even': [], 'odd': []}

categorize_numbers([100, 25, 7, 42])
คืนค่า: {'even': [100, 42], 'odd': [25, 7]} 
'''

def categorize_numbers(numbers):
	return {
		'even': [i for i in numbers if i%2 == 0],
		'odd': [i for i in numbers if i%2 != 0]
		}

result = categorize_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)