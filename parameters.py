class Parameters:
    def __init__(self):
        self.n_tiles_x = 30
        self.n_tiles_y = 20
        self.tile_size = 40
        self.min_window_width = 400
        self.min_window_height = 400

    def get_n_tiles_x(self):
        return self.n_tiles_x
    
    def get_n_tiles_y(self):
        return self.n_tiles_y
    
    def get_tile_size(self):
        return self.tile_size
    
    def get_min_window_width(self):
        return self.min_window_width
    
    def get_min_window_height(self):
        return self.min_window_height
    
    def set_tile_size(self, tile_size):
        self.tile_size = tile_size
    
