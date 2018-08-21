# -*- coding: utf-8 -*-


from ustoolbox.utils.command import run_win, list_directories, list_files, purge


if __name__ == '__main__':

    run_win('C:/Users/Edgar/PlusApp-2.6.0.20180120-Win32/bin/EditSequenceFile.exe')

    base_dir = 'C:/Users/Edgar/Desktop/US'
    print(list_directories(base_dir))

    base_dir = 'C:/Users/Edgar/Desktop/US/FA'
    print(list_files(base_dir, '.mha'))

    purge('D:/US_TEST/GT', 'CROP')
    purge('D:/US_TEST/GT', 'VOLUME')
