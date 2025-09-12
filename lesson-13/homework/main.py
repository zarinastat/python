{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7fb0b51a",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "time data '' does not match format '%Y-%m-%d'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mdatetime\u001b[39;00m  \u001b[38;5;66;03m# datetime modulini import qilamiz\u001b[39;00m\n\u001b[32m      3\u001b[39m dob_str = \u001b[38;5;28minput\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mTug‘ilgan sanangizni kiriting (YYYY-MM-DD): \u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m dob = \u001b[43mdatetime\u001b[49m\u001b[43m.\u001b[49m\u001b[43mdatetime\u001b[49m\u001b[43m.\u001b[49m\u001b[43mstrptime\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdob_str\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43m%\u001b[39;49m\u001b[33;43mY-\u001b[39;49m\u001b[33;43m%\u001b[39;49m\u001b[33;43mm-\u001b[39;49m\u001b[38;5;132;43;01m%d\u001b[39;49;00m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m.date()  \u001b[38;5;66;03m# datetime.datetime ni ishlatish\u001b[39;00m\n\u001b[32m      5\u001b[39m today = datetime.date.today()  \u001b[38;5;66;03m# date.today() o'rniga datetime.date.today() ishlatish\u001b[39;00m\n\u001b[32m      7\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mTug‘ilgan sanangiz: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mdob\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\_strptime.py:653\u001b[39m, in \u001b[36m_strptime_datetime\u001b[39m\u001b[34m(cls, data_string, format)\u001b[39m\n\u001b[32m    650\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34m_strptime_datetime\u001b[39m(\u001b[38;5;28mcls\u001b[39m, data_string, \u001b[38;5;28mformat\u001b[39m=\u001b[33m\"\u001b[39m\u001b[38;5;132;01m%a\u001b[39;00m\u001b[33m \u001b[39m\u001b[33m%\u001b[39m\u001b[33mb \u001b[39m\u001b[38;5;132;01m%d\u001b[39;00m\u001b[33m \u001b[39m\u001b[33m%\u001b[39m\u001b[33mH:\u001b[39m\u001b[33m%\u001b[39m\u001b[33mM:\u001b[39m\u001b[33m%\u001b[39m\u001b[33mS \u001b[39m\u001b[33m%\u001b[39m\u001b[33mY\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m    651\u001b[39m \u001b[38;5;250m    \u001b[39m\u001b[33;03m\"\"\"Return a class cls instance based on the input string and the\u001b[39;00m\n\u001b[32m    652\u001b[39m \u001b[33;03m    format string.\"\"\"\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m653\u001b[39m     tt, fraction, gmtoff_fraction = \u001b[43m_strptime\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdata_string\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mformat\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m    654\u001b[39m     tzname, gmtoff = tt[-\u001b[32m2\u001b[39m:]\n\u001b[32m    655\u001b[39m     args = tt[:\u001b[32m6\u001b[39m] + (fraction,)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\_strptime.py:432\u001b[39m, in \u001b[36m_strptime\u001b[39m\u001b[34m(data_string, format)\u001b[39m\n\u001b[32m    430\u001b[39m found = format_regex.match(data_string)\n\u001b[32m    431\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m found:\n\u001b[32m--> \u001b[39m\u001b[32m432\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[33m\"\u001b[39m\u001b[33mtime data \u001b[39m\u001b[38;5;132;01m%r\u001b[39;00m\u001b[33m does not match format \u001b[39m\u001b[38;5;132;01m%r\u001b[39;00m\u001b[33m\"\u001b[39m %\n\u001b[32m    433\u001b[39m                      (data_string, \u001b[38;5;28mformat\u001b[39m))\n\u001b[32m    434\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(data_string) != found.end():\n\u001b[32m    435\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[33m\"\u001b[39m\u001b[33munconverted data remains: \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[33m\"\u001b[39m %\n\u001b[32m    436\u001b[39m                       data_string[found.end():])\n",
      "\u001b[31mValueError\u001b[39m: time data '' does not match format '%Y-%m-%d'"
     ]
    }
   ],
   "source": [
    "\n",
    "import datetime  # datetime modulini import qilamiz\n",
    "\n",
    "dob_str = input(\"Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): \")\n",
    "dob = datetime.datetime.strptime(dob_str, \"%Y-%m-%d\").date()  # datetime.datetime ni ishlatish\n",
    "today = datetime.date.today()  # date.today() o'rniga datetime.date.today() ishlatish\n",
    "\n",
    "print(f\"Tug‘ilgan sanangiz: {dob}\")\n",
    "print(f\"Bugungi sana: {today}\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f6d49ae3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'today' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m years = \u001b[43mtoday\u001b[49m.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))\n\u001b[32m      2\u001b[39m months = (today.year - dob.year) * \u001b[32m12\u001b[39m + today.month - dob.month\n\u001b[32m      3\u001b[39m days = (today - dob).days\n",
      "\u001b[31mNameError\u001b[39m: name 'today' is not defined"
     ]
    }
   ],
   "source": [
    "years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))\n",
    "months = (today.year - dob.year) * 12 + today.month - dob.month\n",
    "days = (today - dob).days\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4f4a7ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sizning yoshingiz: 39 yil, 475 oy, 14446 kun\n"
     ]
    }
   ],
   "source": [
    "print(f\"Sizning yoshingiz: {years} yil, {months} oy, {days} kun\")\n",
    "dob_str = input(\"Tug‘ilgan kuningiz (YYYY-MM-DD): \")\n",
    "dob = datetime.strptime(dob_str, \"%Y-%m-%d\").date()\n",
    "today = DATETIME.date.today()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3fb87db8",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'dob' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m next_birthday = \u001b[43mdob\u001b[49m.replace(year=today.year)\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m next_birthday < today:\n\u001b[32m      3\u001b[39m     next_birthday = next_birthday.replace(year=today.year + \u001b[32m1\u001b[39m)\n",
      "\u001b[31mNameError\u001b[39m: name 'dob' is not defined"
     ]
    }
   ],
   "source": [
    "next_birthday = dob.replace(year=today.year)\n",
    "if next_birthday < today:\n",
    "    next_birthday = next_birthday.replace(year=today.year + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "682abbcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "days_left = (next_birthday - today).days\n",
    "print(f\"Keyingi tug‘ilgan kuningizga {days_left} kun qoldi 🎉\")\n",
    "from datetime import timedelta\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4c86788",
   "metadata": {},
   "outputs": [],
   "source": [
    "now_str = input(\"Hozirgi sana va vaqt (YYYY-MM-DD HH:MM): \")\n",
    "now = datetime.strptime(now_str, \"%Y-%m-%d %H:%M\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1b2f258",
   "metadata": {},
   "outputs": [],
   "source": [
    "hours = int(input(\"Uchrashuv davomiyligi (soat): \"))\n",
    "minutes = int(input(\"Uchrashuv davomiyligi (daqiqa): \"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85a3e554",
   "metadata": {},
   "outputs": [],
   "source": [
    "end_time = now + timedelta(hours=hours, minutes=minutes)\n",
    "print(\"Uchrashuv tugash vaqti:\", end_time)\n",
    "from datetime import datetime\n",
    "import pytz\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9ba5cff",
   "metadata": {},
   "outputs": [],
   "source": [
    "dt = datetime.strptime(dt_str, \"%Y-%m-%d %H:%M\")\n",
    "from_tz = pytz.timezone(from_zone)\n",
    "to_tz = pytz.timezone(to_zone)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dt_local = from_tz.localize(dt)\n",
    "dt_converted = dt_local.astimezone(to_tz)\n",
    "\n",
    "print(\"Natija:\", dt_converted.strftime(\"%Y-%m-%d %H:%M\"))\n",
    "import time\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c2085fcc",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'datetime' has no attribute 'strptime'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m future_str = \u001b[38;5;28minput\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mKelajakdagi sana va vaqt (YYYY-MM-DD HH:MM:SS): \u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m future = \u001b[43mdatetime\u001b[49m\u001b[43m.\u001b[49m\u001b[43mstrptime\u001b[49m(future_str, \u001b[33m\"\u001b[39m\u001b[33m%\u001b[39m\u001b[33mY-\u001b[39m\u001b[33m%\u001b[39m\u001b[33mm-\u001b[39m\u001b[38;5;132;01m%d\u001b[39;00m\u001b[33m \u001b[39m\u001b[33m%\u001b[39m\u001b[33mH:\u001b[39m\u001b[33m%\u001b[39m\u001b[33mM:\u001b[39m\u001b[33m%\u001b[39m\u001b[33mS\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mAttributeError\u001b[39m: module 'datetime' has no attribute 'strptime'"
     ]
    }
   ],
   "source": [
    "future_str = input(\"Kelajakdagi sana va vaqt (YYYY-MM-DD HH:MM:SS): \")\n",
    "future = datetime.strptime(future_str, \"%Y-%m-%d %H:%M:%S\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66eb2eaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    now = datetime.now()\n",
    "    if now >= future:\n",
    "        print(\"⏰ Vaqt tugadi!\")\n",
    "        break\n",
    "    remaining = future - now\n",
    "    print(\"Qolgan vaqt:\", remaining, end=\"\\r\")\n",
    "    time.sleep(1)\n",
    "import re\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7aba33bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "email = input(\"Emailni kiriting: \")\n",
    "pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70c3c1ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "if re.match(pattern, email):\n",
    "    print(\"✅ To‘g‘ri email manzil\")\n",
    "else:\n",
    "    print(\"❌ Noto‘g‘ri email manzil\")\n",
    "num = input(\"Telefon raqam kiriting (faqat raqamlar): \")\n",
    "\n",
    "if len(num) == 10 and num.isdigit():\n",
    "    formatted = f\"({num[:3]}) {num[3:6]}-{num[6:]}\"\n",
    "    print(\"Formatlangan raqam:\", formatted)\n",
    "else:\n",
    "    print(\"❌ 10 ta raqam kiriting\")\n",
    "import re\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43d7ce95",
   "metadata": {},
   "outputs": [],
   "source": [
    "password = input(\"Parolni kiriting: \")\n",
    "\n",
    "if (len(password) >= 8 and\n",
    "    re.search(r'[A-Z]', password) and\n",
    "    re.search(r'[a-z]', password) and\n",
    "    re.search(r'[0-9]', password)):\n",
    "    print(\"✅ Kuchli parol\")\n",
    "else:\n",
    "    print(\"❌ Parol kuchsiz (kamida 8 belgidan iborat, katta-harflar, kichik-harflar va raqam bo‘lishi kerak)\")\n",
    "text = \"Python is powerful. Python is easy to learn. Python is everywhere.\"\n",
    "word = input(\"Qidiriladigan so‘z: \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "56b0728b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'text' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m positions = [i \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;28mlen\u001b[39m(\u001b[43mtext\u001b[49m.split())) \u001b[38;5;28;01mif\u001b[39;00m text.split()[i].lower() == word.lower()]\n\u001b[32m      2\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33m'\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mword\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m'\u001b[39m\u001b[33m so‘zi \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mlen\u001b[39m(positions)\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m marta topildi. Indekslar:\u001b[39m\u001b[33m\"\u001b[39m, positions)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mre\u001b[39;00m\n",
      "\u001b[31mNameError\u001b[39m: name 'text' is not defined"
     ]
    }
   ],
   "source": [
    "positions = [i for i in range(len(text.split())) if text.split()[i].lower() == word.lower()]\n",
    "print(f\"'{word}' so‘zi {len(positions)} marta topildi. Indekslar:\", positions)\n",
    "import re\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "955ff7d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "text = input(\"Matn kiriting (masalan: Today is 2025-09-10, tomorrow is 2025/09/11): \")\n",
    "dates = re.findall(r'\\d{4}[-/]\\d{2}[-/]\\d{2}', text)\n",
    "\n",
    "print(\"Topilgan sanalar:\", dates)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
