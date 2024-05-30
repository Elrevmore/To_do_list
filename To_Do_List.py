tasks = []
# Görev ekleme fonksiyonu

def add_task(task):
  tasks.append(task)
  print(f"Görev eklendi: {task}")

# Görevleri listeleme fonksiyonu
def list_tasks():
  if not tasks:
    print("Görev listesi boş.")
  else:
    print("Görev listesi:")
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")

# Ana menü fonksiyonu
def main_menu():
  while True:
    print("\n--- To_Do Listesi Uygulamasi---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Çikiş")
    choice = input("Seçiminizi yapiniz: ")

    if choice == "1":
      task = input("Yeni görevi giriniz: ")
      add_task(task)

    elif choice == "2":
      list_tasks()
    elif choice == "3":
      print("Çikiliyor...")
      break
    else:
      print("Geçersiz seçim. Tekrar deneyiniz.")

# Ana menüyü başlatıyoruz
main_menu()

import json

# Görevleri dosyaya kaydetme 
def save_tasks(filename="tasks.json"):
  with open(filename, "w") as f:
    json.dump(tasks,f)
  print("Görevler kaydedildi")

# Görevleri dosyadan yükleme
def load_tasks(filename="tasks.json"):
  global tasks
  try:
    with open(filename, "r") as f:
      tasks = json.load(f)
    print("Görevler yüklendi.")
  except FileNotFoundError:
    print("Kaydedilmiş görev bulunamadi.")

# Ana menü fonksiyonlarını güncelleme
def main_menu():
  load_tasks()

  while True:
    print("\n--- To_Do Listesi Uygulamasi---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Çikiş")
    choice = input("Seçiminizi yapiniz: ")

    if choice == "1":
      task = input("Yeni görevi giriniz.")
      add_task(task)

    elif choice == "2":
       list_tasks()
    elif choice == "3":
      print("Çikiliyor...")
      break
    else:
      print("Geçersiz seçim. Tekrar deneyiniz.")

main_menu()

def add_task(task):
  tasks.append({"task": task, "completed": False})
  print(f"Görev eklendi: {task}")

def list_tasks():
  if not tasks:
    print("Görev listesi boş.")
  else:
    print("Görev listesi:")
    for i, task in enumerate(tasks, 1):
      status = "Tamamlandi" if task["complered"] else "Devam ediyor"
      print(f"{i}. {task['task']} [{status}]")

def complete_task(index):
  try:
    tasks[index]["completed"] = True
    print(f"Görev tamamlandi: {tasks[index]["task"]}")
  except IndexError:
    print("Geçersiz görev numarasi.")

def main_menu():
  load_tasks()
  while True:
    print("\n--- To_Do Listesi Uygulamasi---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Çikiş")
    choice = input("Seçiminizi yapiniz: ")

    if choice == "1":
      task = input("Yeni görevi giriniz.")
      add_task(task)
    elif choice == "2":
       list_tasks()
    elif choice == "3":
      list_tasks()
      index = int(input("Tamamlanmış olarak isaretlemek istediğiniz görevi numarısını giriniz: ")) -1
      complete_task(index)
    elif choice == "4":
      save_tasks()
      print("Çıkılıyor...")
      break
    else:
      print("Geçersiz seçim. Tekrar deneyiniz.")

main_menu()
def delete_task(index):
  try:
    removed_task = tasks.pop(index)
    print(f"Görev silindi: {removed_task["task"]}")
  except IndexError:
    print("Geçersiz görev numarasi.")

def clear_completed_tasks():
  global tasks
  tasks = [task for task in tasks if not task["completed"]]
  print("Tamamlanmış görevler temizlendi.")

def main_menu():
  load_tasks()

  while True:
    print("\n--- To_Do Listesi Uygulamasi---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. görevi Tamamla")
    print("4. Görev Sil")
    print("5. Tamamlanmış Görevleri Temizle")
    print("6. Görevleri Kaydet ve Çık")
    choice = input("Seçiminizi yapınız:")

    if choice == "1":
      task = input("Yeni görevi giriniz:")
      add_task(task)
    elif choice == "2":
       list_tasks()
    elif choice == "3":
      list_tasks()
      index = int(input("Tamamlanmış olarak isaretlemek istediğiniz görevi numarısını giriniz: ")) -1
      complete_task(index)
    elif choice == "4":
      list_tasks()
      index = int(input("Silmek istediğiniz görevin numarasını giriniz:")) - 1
      delete_task(index)
    elif choice == "5":
      clear_completed_tasks()
    elif choice == "6":
      save_tasks()
      print("Çıkılıyor...")
      break
    else:
      print("Geçersiz seçim. Tekrar deneyiniz")

main_menu






        
