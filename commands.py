import os
import settings

def clear_folders(folders, force=True):
    # клон rm линупса
    if len(folders) != 0: 
        for folder in settings.CLEANED_FOLDERS:
            for deleted_file in os.listdir(folder):
                if not force:
                    if input("remove: " + deleted_file + " in " + folder + "? (y/n) "):
                        pass
                    else:
                        continue
                os.remove(os.path.join(folder, deleted_file))
    return "clear"