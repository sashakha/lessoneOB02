class User:
  def __init__(self, user_id, name, access_level='user'):
      self._user_id = user_id
      self._name = name
      self._access_level = access_level

  @property
  def user_id(self):
      return self._user_id

  @user_id.setter
  def user_id(self, value):
      self._user_id = value

  @property
  def name(self):
      return self._name

  @name.setter
  def name(self, value):
      self._name = value

  @property
  def access_level(self):
      return self._access_level

  @access_level.setter
  def access_level(self, value):
      self._access_level = value


class Admin(User):
  def __init__(self, user_id, name):
      super().__init__(user_id, name, access_level='admin')
      self._users_list = []

  def add_user(self, user):
      if user not in self._users_list:
          self._users_list.append(user)
          print(f"User {user.name} added.")
      else:
          print("User is already in the list.")

  def remove_user(self, user):
      if user in self._users_list:
          self._users_list.remove(user)
          print(f"User {user.name} removed.")
      else:
          print("User not found in the list.")

  def display_users(self):
      if self._users_list:
          print("Users list:")
          for user in self._users_list:
              print(f"ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")
      else:
          print("No users in the list.")


if __name__ == "__main__":
  user1 = User("1", "Андрей")
  user2 = User("2", "Геннадий")

  print(f"User1: ID={user1.user_id}, Name={user1.name}, Access Level={user1.access_level}")
  print(f"User2: ID={user2.user_id}, Name={user2.name}, Access Level={user2.access_level}")

  admin = Admin("100", "Вероника")

  admin.add_user(user1)
  admin.add_user(user2)

  print("\nПользователи после добавления:")
  admin.display_users()

  admin.remove_user(user1)

  print("\nПользователи после удаления:")
  admin.display_users()

  user2.name = "Борис"
  print(f"\nUser2 после изменения имени: Имя={user2.name}")
