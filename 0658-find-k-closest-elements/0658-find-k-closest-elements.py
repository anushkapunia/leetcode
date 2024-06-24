class Solution(object):
    def findClosestElements(self, arr, k, x):
     
        left = 0
        right = len(arr) - k
    
        # Двоичный поиск для определения начальной позиции окна из k элементов
        while left < right:
            mid = left + (right - left) // 2
            # Сравниваем расстояние от середины текущего окна до x
            # с расстоянием от середины следующего (mid + k) окна до x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1  # Сдвигаем левую границу вправо
            else:
                right = mid  # Сдвигаем правую границу влево
        
        # Возвращаем k ближайших элементов, начиная с позиции left
        return arr[left:left + k]