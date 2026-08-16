from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):

        n = len(image)
        m = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        q = deque([(sr, sc)])

        image[sr][sc] = color

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:

            x, y = q.popleft()

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if (0 <= nx < n and 
                    0 <= ny < m and 
                    image[nx][ny] == original):

                    image[nx][ny] = color
                    q.append((nx, ny))

        return image