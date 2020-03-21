start_command_response = "Привет 👋🏼! Я могу помочь вам с планированием ваших дел. А точнее, я буду напоминать вам о ваших делах, которые вы запишете у меня." \
"\n" \
"\n" \
"Для ознакомления со всеми функциями введите /help." \
"\n" \
"\n" \
"Также, если у вас есть жалобы/предложения разработчикам, используйте /feedback. 📝" \
"\n" \
"\n" \
"Удачи и продуктивности! 👨🏻‍💻"

help_command_response = "Доступные команды:" \
"\n" \
"\n" \
"1. /add <Новое задание> - Добавить новое задание в список дел." \
"\n" \
"2. /delete <Номер задания> - удалить определенное задание." \
"\n" \
"3. /showtasks - Показать все ваши задания." \
"\n" \
"4. /set X <кол-во минут> - выбрать время и включить таймер. Каждые X минут я буду отправлять вам список ваших дел." \
"\n" \
"5. /stop - остановить таймер." \
"\n" \
"6. /clear - Очистить весь ваш список." \
"\n" \
"7. /feedback - Отправить предложение/жалобу разработчику" \
"\n" \
"8. /help - Список всех доступных команд."

clear_command_confirmation = "Вы уверены что хотите очистить весь ваш список задач? 🗑"

feedback_success_command_response = "Удачно отправил ваш фидбэк всем админам 🥳"

feedback_error_command_response = "/feedback <текст>"

send_to_all_success_command_response = "Удачно отправил ваше сообщение 🥳"

admin_help_command_response = "Доступные команды для админов: " \
"\n" \
"\n" \
"1. /admin_send_to_all <текст> - Отправить <текст> всем юзерам бота." \
"\n" \
"\n" \
"2. /admin_get_distinct - Получить количество юзеров бота." \
"\n" \
"\n" \
"3. /admin_send_to <User ID> <текст> - Отправить текст определенному юзеру." \
"\n" \
"\n" \
"4. /admin_help - Список всех доступных команд для админов." \

cancelled_successfully = "Ну ладно 🙃, надеюсь еще смогу помочь вам..."

unknown_command_response = "Извините 😬, но я не знаю эту команду. Чтобы ознакомиться со всеми командами бота пропишите /help."

stopped_successfully_command_response = "Таймер выключен 😴"

did_not_set_command_response = "Таймер не был включен 😴"

error_time_command_response = "Количество минут должно быть от 1 до 14400 🤨"

set_timer_successfully_command_response = "Вы удачно завели таймер 🥳." \
"\n" \
"\n" \
"Чтобы остановить его, пропишите /stop"

updated_timer_successfully_command_response = "Вы удачно обновили таймер 🥳." \
"\n" \
"\n" \
"Чтобы остановить его, пропишите /stop"

checking_todo_list_words = "Хей 🤗, давайте пройдемся по вашему списку, может вы что-то уже из этого сделали?\n\nВот ваш список дел:\n"

checked_todo_list_words = "\nЕсли вы выполнили что-то из этого, используйте /delete чтобы удалить задание 😉"

set_timer_error_command_response = "/set <кол-во минут>."

add_task_successfully_command_response = "/add <Новое задание>"

add_task_write_task = "Хорошо, введите задание которое хотите добавить в список 🗒:" \
"\n" \
"\n" \
"/cancel - отменить операцию."

delete_task_write_task = "Окей, выберите задание которое нужно удалить 🗑:" \
"\n" \
"\n" \
"/cancel - отменить операцию."

set_timer_write_time = "Вас понял, через каждые сколько минут мне вас уведомлять о ваших задачах?: ⏰" \
"\n" \
"\n" \
"/cancel - отменить операцию."

feedback_write_text = "Окей, введите ваше предложение/жалобу ниже: 📝" \
"\n" \
"\n" \
"/cancel - отменить операцию."

delete_task_successfully_command_response = "Вы удачно удалили это задание 😌"

delete_task_error_command_response = "/delete <Номер задания> - удалить определенное задание."

delete_task_wrong_number_command_response = "Я не нашел задание с таким номером 🤨"

clear_successfully_command_response = "Вы успешно очистили список ваших дел 🥳"

guide_set_timer = "Круто 🥳! Вы можете поставить таймер используя команду /set."

tasks_empty_command_response = "Извините, но ваш список пустой 😌"

show_tasks_command_response = "Хорошо , вот ваш список задач: " \
"\n" \
"\n"

updated_tasks_command_response = "Отлично 🤗! Вот ваш обновленный список задач:" \
"\n" \
"\n"

send_to_all_error_command_response = "/admin_send_to_all <Текст для отправки>"

send_to_error_command_response = "/admin_send_to <User ID> <Текст для отправки>"

choose_language_command_response = "🇷🇺Привет, для начала давай выберем язык: " \
"\n" \
"\n" \
"🇺🇸Hi, let's choose the language first:"
