import random
from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

bot = Bot("6005481092:AAFT4kGkrsx4X4bNLfF8XoO4Ou7pIcH44E8")
dp = Dispatcher(bot=bot,storage=MemoryStorage())

def umn(ras):
    n1=random.randint(int("1"+"0"*(ras-1)),int("10"+"0"*(ras-1)))
    n2=random.randint(int("1"+"0"*(ras-1)),int("10"+"0"*(ras-1)))
    inp = str(n1)+"*"+str(n2)
    rest = n1*n2
    return inp,rest
class number(StatesGroup):
    wait_type = State()
    wait_count = State()
    wait_answer = State()
@dp.message_handler(commands=['start'])
async def start(mes:types.Message,state:FSMContext):
    await bot.send_message(mes.from_user.id,"""Добро пожаловать в математическую игру Миссия Невыполнима. Здесь вы можете потренировать свои мозги под умножежение, сложение, вычитание. Выберете режим:
Введите 1 для умножения.
Введите 2 для сложения - вычитания.
Введите 3 для нереально трудного режима все в перемешку""")
    await state.set_state(number.wait_type.state)
@dp.message_handler(state=number.wait_type)
async def type(mes: types.Message,state: FSMContext):
    if mes.text=="":
        await mes.answer("Поле пустое, попробуйте еще раз:")
        return
    await state.update_data(type=int(mes.text))
    await mes.answer("Сколько разрядов вам для первого раза?")
    await state.set_state(number.wait_count.state)
@dp.message_handler(state=number.wait_count)
async def count(mes: types.Message,state: FSMContext):
    if mes.text=="":
        await mes.answer("Поле пустое, попробуйте еще раз:")
        return
    await state.update_data(count=int(mes.text))
    global inp
    #user_type = state.get_data()["type"]
    """if user_type == 1:
        inp = umn(mes.text)
    else:
        inp= "Sorry"""
    inp = umn(int(mes.text))
    await mes.answer(inp[0])
    await state.set_state(number.wait_answer.state)
@dp.message_handler(state=number.wait_answer)
async def answer(mes: types.Message,state: FSMContext):
    if mes.text=="":
        await mes.answer("Поле пустое, попробуйте еще раз:")
        return
    if int(mes.text)==inp[1]:
        await mes.answer("T")
    else:
        await mes.answer("F")
    await state.finish()
if __name__ == '__main__':
    executor.start_polling(dp)
