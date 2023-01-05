names = ["Rzeszów", "Kraków", "Katowice", "Wrocław", "Lublin", "Łódź", "Warszawa", "Białystok", "Gdańsk", "Szczecin"]
distances = [[0, 110, 170, 280, 160, 320, 310, 460, 440, 600],
             [110, 0, 50, 180, 300, 180, 150, 320, 380, 540],
             [170, 50, 0, 120, 280, 180, 180, 380, 420, 440],
             [280, 180, 120, 0, 390, 190, 270, 450, 300, 270],
             [160, 300, 280, 390, 0, 240, 135, 300, 330, 720],
             [320, 180, 180, 190, 240, 0, 150, 260, 290, 420],
             [310, 150, 180, 270, 135, 150, 0, 150, 150, 440],
             [460, 320, 380, 450, 300, 260, 150, 0, 340, 720],
             [440, 380, 420, 300, 330, 290, 150, 340, 0, 280],
             [600, 540, 440, 270, 720, 420, 440, 720, 280, 0]]

cities_probabilities = [[0,    0.2,  0.09, 0.07, 0.15, 0.12, 0.1,  0.14, 0.05, 0.08],
                        [0.2,  0,    0.15, 0.09, 0.14, 0.05, 0.12, 0.08, 0.07, 0.1],
                        [0.09, 0.15, 0,    0.14, 0.05, 0.2,  0.08, 0.07, 0.1,  0.12],
                        [0.07, 0.09, 0.14, 0,    0.2,  0.14, 0.15, 0.1,  0.08, 0.05],
                        [0.15, 0.14, 0.05, 0.2,  0,    0.1,  0.05,  0.12, 0.09, 0.07],
                        [0.12, 0.05, 0.2,  0.12, 0.1,  0,    0.09, 0.15, 0.2,  0.14],
                        [0.1,  0.12, 0.08, 0.15, 0.08, 0.09, 0,    0.05, 0.14, 0.2],
                        [0.14, 0.08, 0.07, 0.1,  0.12, 0.08, 0.14, 0,    0.15, 0.09],
                        [0.05, 0.07, 0.1,  0.08, 0.09, 0.07, 0.07, 0.09, 0,    0.15],
                        [0.08, 0.1,  0.12, 0.05, 0.07, 0.15, 0.2,  0.2,  0.12, 0]]

cities = []
cities_elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

transfer_elements = [1, 2, 3, 4, 5]
transfer_probabilities = [0.1, 0.2, 0.15, 0.25, 0.3]

total_time = []

route = [0]
