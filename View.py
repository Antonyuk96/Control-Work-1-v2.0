class View(object):
     @staticmethod
     def show_number_point_list(notes):
         for note in notes:
             print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                  + Style.RESET_ALL)
             print(note)
             print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                  + Style.RESET_ALL)
              @staticmethod
              def show_note(note):
                  print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
                  print(note)
                  print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
                  @staticmethod
                  def show_empty_list_message():
                      print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
                      print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
                      print('Cписок пуст')
                      print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
                      @staticmethod
                      def display_note_id_not_exist(note_id):
                          print(Fore.RED + '**************************************************************'
              + Style.RESET_ALL)
                          print('Заметка с id: {} не найдена!'.format(note_id))
                          print(Fore.RED + '**************************************************************'
              + Style.RESET_ALL)
                          @staticmethod
                          def display_note_id_exist(note_id):
                              print(Fore.RED + '**************************************************************')
                              print('Заметка с id: {} уже есть'.format(note_id))
                              print('**************************************************************'
              + Style.RESET_ALL)
                              @staticmethod
                              def display_note_stored():
                                  print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
                                  print(Fore.GREEN + 'Заметка добавлена' + Style.RESET_ALL)
                                  print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
                                   @staticmethod
                                   def display_note_updated(note_id):
                                       print(Fore.YELLOW + '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --' + Style.RESET_ALL)
                                       
                              print(Fore.GREEN + 'Заметка с id:{} изменена'.format(note_id) + Style.RESET_ALL)
                              print(Fore.YELLOW + '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --' + Style.RESET_ALL)
                               @staticmethod
                               def display_note_deletion(note_id):
                                   print(Fore.RED + '--------------------------------------------------------------')
                                   print('Все заметки удалены')
                                   print('--------------------------------------------------------------' + Style.RESET_ALL)
                                   def display_note_id_not_exist(search_id):
                                       return search_id
                                    
                              
                                    
