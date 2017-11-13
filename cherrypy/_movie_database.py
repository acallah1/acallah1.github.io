
#Andrew Callahan
#python primer
class _movie_database:

    def __init__(self):
      self.movies = dict()
      self.users = dict()
      self.ratings = dict()

    def load_movies(self, movie_file):
      self.movies=dict()
    	#open fileobject
      with open(movie_file ,'r') as file:
	    #read each line
        for line in file:
          if(len(line)):
                   fields = line.strip().split("::")
                   self.movies[int(fields[0])] = fields[1:]
    def get_movie(self,mid):
      return None if mid not in self.movies else self.movies[mid]
    def get_movies(self):
      return self.movies.keys()
    def set_movie(self , mid, list):
      self.movies[mid]=list
    def delete_movie(self, mid):
      del self.movies[mid]
    def delete_movies(self):
      self.movies = dict()
    def delete_all_ratings(self):
      self.ratings=dict()
    def load_users(self,users_file):
      self.users=dict()
      with open(users_file ,'r') as file:
      #read each line
        for line in file:
          if(len(line)):
                   fields = line.strip().split("::")
                   self.users[int(fields[0])] = fields[1:]
                   self.users[int(fields[0])][1] = int(self.users[int(fields[0])][1])
                   self.users[int(fields[0])][2] = int(self.users[int(fields[0])][2])
    def get_user(self,uid):
      return None if uid not in self.users else self.users[uid]
    def get_users(self):
      return self.users.keys()
    def set_user(self,uid,list):
      self.users[uid]=list
    def delete_user(self,uid):
      del self.users[uid]
    def delete_users(self):
      self.users = dict()
    def load_ratings(self,ratings_file):
      self.ratings=dict()
      with open(ratings_file ,'r') as file:
      #read each line
        for line in file:
          if(len(line)):
                   fields = line.strip().split("::")
                   if int(fields[1]) not in self.ratings:
                     self.ratings[int(fields[1])]=dict()
                   self.ratings[int(fields[1])][int(fields[0])] = float(fields[2])
                    
    def get_rating(self,mid):
      sum=0.0
      count=float(len (self.ratings[mid]))
      for key in self.ratings[mid]:
        sum+=float(self.ratings[mid][key])
        #count+=1.0
      return sum/count
    def get_highest_rated_movie(self):
      max=0.0
      id=0
      for key in sorted(self.ratings):
        rating = self.get_rating(key)
        if rating > max:
          id=key
          max=rating
      return id
    def get_highest_rated_new_movie(self,uid):
      max=0.0
      id=0
      for key in sorted(self.ratings):
        rating = self.get_rating(key)
        if rating > max and uid not in self.ratings[key]:
          id=key
          max=rating
      return id
    def set_user_movie_rating(self,uid,mid,rating):
      if mid in self.ratings:
        self.ratings[mid][uid]=rating
    def get_user_movie_rating(self,uid,mid):
      return self.ratings[mid][uid]

    def load_all(self,ratings_file, users_file,movies_file):
      self.load_ratings(ratings_file)
      self.load_users(users_file)
      self.load_movies(movies_file)

    def load_mid(self, mid,movie_file):
       with open(movie_file ,'r') as file:
       #read each line
          for line in file:
             if(len(line)):
                fields = line.strip().split("::")
                if(int(fields[0]) == mid):
                   self.movies[int(fields[0])] = fields[1:]

