import os
class wrexham:
  def Constructor(self):
    self.__PlayerNumber = ()
    self.__Forename = ()
    self.__Surname = ()
    self.__Position = ()
    self.__CommunityInvolvement = 0
    self.__Injured = False


  def GetPlayerInfo(self):
    try:
      with open("wrexham.txt","r") as t:
        initial_number = 1
        number = int(input("which player would you like"))
        i = 1
        for lines in t:
          if i == 1:
            self.__PlayerNumber = lines
            if initial_number == number:
              print(self.__PlayerNumber)
              return self.__PlayerNumber
          if i == 2:
            self.__Forename = lines
            if initial_number == number:
              print(self.__Forename)
              return self.__Forename
          if i == 3:
            self.__Surname = lines
            if initial_number == number:
              print(self.__Surname)
              return self.__Surname
          if i == 4:
            self.__Position = lines
            ComChange = int(input("How much community involvement have they had"))
            self.ChangeCommunityInvolvement(ComChange)
            InjChange = input("are they hurt(y or n)?")
            self.ChangeInjured()
            i = 1
            initial_number =+ 1



    except OSError:
      print("cant find file, dirrectory is in", os.getcwd())


  def ChangeCommunityInvolvement(self, ComChange):
    self.__CommunityInvolvement = ComChange



  def ChangeInjured(self):
    InjChange = input("are they hurt(y or n)?")
    if InjChange == "y":
      self.__Injured = True
    if InjChange == "n":
      self.__Injured = False


object = wrexham()
object.GetPlayerInfo()
