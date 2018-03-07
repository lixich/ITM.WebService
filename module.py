from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_module = Blueprint('module', __name__)
module_set = [
	# Проект "Сумма"
    {
        "Id": 1,
        "Name": 'Sum(a, b)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 1,
        "MainModuleId": None
    },
    {
        "Id": 2,
        "Name": 'Input(a,b)',
        "CodeLinesNumber": 97,
        "ImportantIndex": 10,
        "RequirementId": 2,
        "MainModuleId": None
    },
    {
        "Id": 3,
        "Name": 'Input(int a, int b)',
        "CodeLinesNumber": 88,
        "ImportantIndex": 10,
        "RequirementId": 3,
        "MainModuleId": None
    },
    {
        "Id": 4,
        "Name": 'Input(real a, real b)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 4,
        "MainModuleId": None
    },
	# Проект "Уравнение"
    {
        "Id": 5,
        "Name": 'Input(a,b,c)',
        "CodeLinesNumber": 97,
        "ImportantIndex": 10,
        "RequirementId": 6,
        "MainModuleId": None
    },
    {
        "Id": 6,
        "Name": 'Input(int a, int b, int c)',
        "CodeLinesNumber": 98,
        "ImportantIndex": 10,
        "RequirementId": 7,
        "MainModuleId": None
    },
    {
        "Id": 7,
        "Name": 'Input(double a, double b, double c)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 8,
        "MainModuleId": None
    },
    {
        "Id": 8,
        "Name": 'SolveEquation()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 9,
        "Name": 'Sum()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 10,
        "Name": 'Deduct()',
        "CodeLinesNumber": 75,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 11,
        "Name": 'Mod()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 12,
        "Name": 'Div()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 13,
        "Name": 'Multiply()',
        "CodeLinesNumber": 230,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 14,
        "Name": 'Sqrt()',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 15,
        "Name": 'Pow()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 16,
        "Name": 'SolveInequality()',
        "CodeLinesNumber": 93,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 17,
        "Name": 'Sum()',
        "CodeLinesNumber": 60,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 18,
        "Name": 'Deduct()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
		"Id": 19, # Почему-то здесь не было этой строки (вдруг так и должно быть)
        "Name": 'Mod()',
        "CodeLinesNumber": 90,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 20,
        "Name": 'Div()',
        "CodeLinesNumber": 95,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 21,
        "Name": 'Multiply()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 22,
        "Name": 'Sqrt()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 23,
        "Name": 'Pow()',
        "CodeLinesNumber": 160,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 24,
        "Name": 'Decision()',
        "CodeLinesNumber": 100,
        "ImportantIndex": 10,
        "RequirementId": 20,
        "MainModuleId": None
    },
    {
        "Id": 25,
        "Name": 'Timer()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 12,
        "MainModuleId": None
    },
    {
        "Id": 26,
        "Name": 'TimerRun(int 10)',
        "CodeLinesNumber": 80,
        "ImportantIndex": 0,
        "RequirementId": 13,
        "MainModuleId": None
    },
    {
        "Id": 27,
        "Name": 'TimerRun(int 20)',
        "CodeLinesNumber": 130,
        "ImportantIndex": 0,
        "RequirementId": 14,
        "MainModuleId": None
    },
    {
        "Id": 28,
        "Name": 'TimerOff()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 0,
        "RequirementId": 15,
        "MainModuleId": None
    },
    {
        "Id": 29,
        "Name": 'Answer()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 16,
        "MainModuleId": None
    },
    {
        "Id": 26,
        "Name": 'ShowChart()',
        "CodeLinesNumber": 110,
        "ImportantIndex": 10,
        "RequirementId": 17,
        "MainModuleId": None
    },
    {
        "Id": 27,
        "Name": 'ShowFormula()',
        "CodeLinesNumber": 130,
        "ImportantIndex": 10,
        "RequirementId": 18,
        "MainModuleId": None
    },
    {
        "Id": 28,
        "Name": 'VoiceAnswer()',
        "CodeLinesNumber": 115,
        "ImportantIndex": 10,
        "RequirementId": 19,
        "MainModuleId": None
    },
    {
        "Id": 29,
        "Name": 'AverageSolving()',
        "CodeLinesNumber": 70,
        "ImportantIndex": 10,
        "RequirementId": 22,
        "MainModuleId": None
    },
    {
        "Id": 30,
        "Name": 'SuccessResult()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 23,
        "MainModuleId": None
    },
    {
        "Id": 31,
        "Name": 'ProcentSuccessResult()',
        "CodeLinesNumber": 60,
        "ImportantIndex": 10,
        "RequirementId": 24,
        "MainModuleId": None
    },
	# Проект "Терминал"
    {
        "Id": 32,
        "Name": 'SaveInfo()',
        "CodeLinesNumber": 70,
        "ImportantIndex": 10,
        "RequirementId": 25,
        "MainModuleId": None
    },
	{
        "Id": 33,
        "Name": 'ConnectDataBase(string database)',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 26,
        "MainModuleId": None
    },
	{
        "Id": 34,
        "Name": 'SaveTicketNumber(int number)',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 27,
        "MainModuleId": None
    },
	{
        "Id": 35,
        "Name": 'ComputeCurrentTicketNumber()',
        "CodeLinesNumber": 15,
        "ImportantIndex": 10,
        "RequirementId": 27,
        "MainModuleId": None
    },
	{
        "Id": 36,
        "Name": 'SaveTicketSeries()',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 28,
        "MainModuleId": None
    },
	{
        "Id": 37,
        "Name": 'SaveSaleDatetime()',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 29,
        "MainModuleId": None
    },
	{
        "Id": 38,
        "Name": 'SavePathNumber()',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 30,
        "MainModuleId": None
    },
	{
        "Id": 39,
        "Name": 'SaveConductorID()',
        "CodeLinesNumber": 30,
        "ImportantIndex": 10,
        "RequirementId": 31,
        "MainModuleId": None
    },
	{
        "Id": 40,
        "Name": 'PushDayInfo()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 32,
        "MainModuleId": None
    },
	{
        "Id": 41,
        "Name": 'ConnectDataBase(string database)',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 33,
        "MainModuleId": None
    },
	{
        "Id": 42,
        "Name": 'PushTicketNumber()',
        "CodeLinesNumber": 70,
        "ImportantIndex": 10,
        "RequirementId": 34,
        "MainModuleId": None
    },
	{
        "Id": 43,
        "Name": 'PushTicketSeries()',
        "CodeLinesNumber": 90,
        "ImportantIndex": 10,
        "RequirementId": 35,
        "MainModuleId": None
    },
	{
        "Id": 44,
        "Name": 'PushSaleDatetime()',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 36,
        "MainModuleId": None
    },
	{
        "Id": 45,
        "Name": 'PushPathNumber()',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 37,
        "MainModuleId": None
    },
	{
        "Id": 46,
        "Name": 'PushConductorID()',
        "CodeLinesNumber": 60,
        "ImportantIndex": 10,
        "RequirementId": 38,
        "MainModuleId": None
    },
	{
        "Id": 47,
        "Name": 'PrintTicket()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 39,
        "MainModuleId": None
    },
	{
        "Id": 48,
        "Name": 'GetPrinterDeviceContext(IntPtr context)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 39,
        "MainModuleId": None
    },
	{
        "Id": 49,
        "Name": 'PrintCompany(string company)',
        "CodeLinesNumber": 25,
        "ImportantIndex": 10,
        "RequirementId": 40,
        "MainModuleId": None
    },
	{
        "Id": 50,
        "Name": 'PrintИНН(string ИНН)',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 41,
        "MainModuleId": None
    },
	{
        "Id": 51,
        "Name": 'PrintTicketNumber(int number)',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 42,
        "MainModuleId": None
    },
	{
        "Id": 52,
        "Name": 'PrintTicketSeries(string series)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 43,
        "MainModuleId": None
    },
	{
        "Id": 53,
        "Name": 'PrintSaleDatetime()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 44,
        "MainModuleId": None
    },
	{
        "Id": 54,
        "Name": 'PrintTicketPrice(double price)',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 45,
        "MainModuleId": None
    },
	{
        "Id": 55,
        "Name": 'PrintPathNumber(int path)',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 46,
        "MainModuleId": None
    },
	{
        "Id": 56,
        "Name": 'PrintConductorID()',
        "CodeLinesNumber": 75,
        "ImportantIndex": 10,
        "RequirementId": 47,
        "MainModuleId": None
    },
	{
        "Id": 57,
        "Name": 'ConvertIDToSafeNumber()',
        "CodeLinesNumber": 100,
        "ImportantIndex": 10,
        "RequirementId": 47,
        "MainModuleId": None
    },
	{
        "Id": 58,
        "Name": 'PrintTransportType(enum)',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 48,
        "MainModuleId": None
    },
	{
        "Id": 59,
        "Name": 'Enum { Bus }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 49,
        "MainModuleId": None
    },
	{
        "Id": 60,
        "Name": 'Enum { TrolleyBus }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 50,
        "MainModuleId": None
    },
	{
        "Id": 61,
        "Name": 'Enum { Tram }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 51,
        "MainModuleId": None
    },
	{
        "Id": 62,
        "Name": 'PrintWarning(string warning)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 52,
        "MainModuleId": None
    },
	{
        "Id": 63,
        "Name": 'PrintAdevrt()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 53,
        "MainModuleId": None
    },
	{
        "Id": 64,
        "Name": 'SetPathInfo()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 54,
        "MainModuleId": None
    },
	{
        "Id": 65,
        "Name": 'SetPathNumber(string number)',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 55,
        "MainModuleId": None
    },
	{
        "Id": 66,
        "Name": 'SetConductorID(GUID id)',
        "CodeLinesNumber": 70,
        "ImportantIndex": 10,
        "RequirementId": 56,
        "MainModuleId": None
    },
	{
        "Id": 67,
        "Name": 'ConfirmConductorID()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 56,
        "MainModuleId": None
    },
	{
        "Id": 68,
        "Name": 'InitDevice()',
        "CodeLinesNumber": 240,
        "ImportantIndex": 10,
        "RequirementId": 57,
        "MainModuleId": None
    },
	{
        "Id": 69,
        "Name": 'LoadInfo()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 10,
        "RequirementId": 57,
        "MainModuleId": None
    },
	{
        "Id": 70,
        "Name": 'ConfirmData()',
        "CodeLinesNumber": 160,
        "ImportantIndex": 10,
        "RequirementId": 57,
        "MainModuleId": None
    },
	{
        "Id": 71,
        "Name": 'SetTicketNumberZero()',
        "CodeLinesNumber": 10,
        "ImportantIndex": 10,
        "RequirementId": 58,
        "MainModuleId": None
    },
	{
        "Id": 72,
        "Name": 'CheckTicketNumber()',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 59,
        "MainModuleId": None
    },
	{
        "Id": 73,
        "Name": 'CheckPathNumber()',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 59,
        "MainModuleId": None
    },
	{
        "Id": 74,
        "Name": 'CheckConductorID()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 59,
        "MainModuleId": None
    },
	{
        "Id": 75,
        "Name": 'SetAdvert(Image advert)',
        "CodeLinesNumber": 190,
        "ImportantIndex": 10,
        "RequirementId": 60,
        "MainModuleId": None
    },
	{
        "Id": 76,
        "Name": 'SetAdvertTimeLimit(int days)',
        "CodeLinesNumber": 30,
        "ImportantIndex": 10,
        "RequirementId": 60,
        "MainModuleId": None
    },
	{
        "Id": 77,
        "Name": 'CheckAdvertTimeLimit()',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 60,
        "MainModuleId": None
    },
	{
        "Id": 78,
        "Name": 'Warn()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 61,
        "MainModuleId": None
    },
	{
        "Id": 79,
        "Name": 'NeedToPushDataWarning()',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 62,
        "MainModuleId": None
    },
	{
        "Id": 80,
        "Name": 'SaveWarningToDatabase()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 62,
        "MainModuleId": None
    },
	{
        "Id": 81,
        "Name": 'NeedToClearDataWarning()',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 63,
        "MainModuleId": None
    },
	{
        "Id": 82,
        "Name": 'CheckDataToClear(double limit)',
        "CodeLinesNumber": 90,
        "ImportantIndex": 10,
        "RequirementId": 63,
        "MainModuleId": None
    },
	{
        "Id": 83,
        "Name": 'SetLimit(double limit)',
        "CodeLinesNumber": 10,
        "ImportantIndex": 10,
        "RequirementId": 63,
        "MainModuleId": None
    },
	{
        "Id": 84,
        "Name": 'SaveWarningToDatabase()',
        "CodeLinesNumber": 130,
        "ImportantIndex": 10,
        "RequirementId": 63,
        "MainModuleId": None
    },
	{
        "Id": 85,
        "Name": 'ReadConductorIDFromScaner(GUID id)',
        "CodeLinesNumber": 340,
        "ImportantIndex": 10,
        "RequirementId": 64,
        "MainModuleId": None
    },
	{
        "Id": 86,
        "Name": 'GetScanerContext(IntPtr context)',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 64,
        "MainModuleId": None
    },
	{
        "Id": 87,
        "Name": 'CheckID(GUID id)',
        "CodeLinesNumber": 70,
        "ImportantIndex": 10,
        "RequirementId": 64,
        "MainModuleId": None
    },
	{
        "Id": 88,
        "Name": 'PrintScreenInfo()',
        "CodeLinesNumber": 100,
        "ImportantIndex": 10,
        "RequirementId": 65,
        "MainModuleId": None
    },
	{
        "Id": 89,
        "Name": 'GetScreenContext(IntPtr context)',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 65,
        "MainModuleId": None
    },
	{
        "Id": 90,
        "Name": 'PrintScreenDatetime()',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 66,
        "MainModuleId": None
    },
	{
        "Id": 91,
        "Name": 'PrintScreenTicketsCount(int count)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 67,
        "MainModuleId": None
    },
	{
        "Id": 92,
        "Name": 'PrintScreenDeviceState(enum)',
        "CodeLinesNumber": 140,
        "ImportantIndex": 10,
        "RequirementId": 68,
        "MainModuleId": None
    },
	{
        "Id": 93,
        "Name": 'Enum { Ready }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 69,
        "MainModuleId": None
    },
	{
        "Id": 94,
        "Name": 'Enum { Payment }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 70,
        "MainModuleId": None
    },
	{
        "Id": 95,
        "Name": 'Enum { Print }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 71,
        "MainModuleId": None
    },
	{
        "Id": 96,
        "Name": 'Enum { Printed }',
        "CodeLinesNumber": 5,
        "ImportantIndex": 10,
        "RequirementId": 72,
        "MainModuleId": None
    },
	{
        "Id": 97,
        "Name": 'ComputePrice()',
        "CodeLinesNumber": 240,
        "ImportantIndex": 10,
        "RequirementId": 73,
        "MainModuleId": None
    },
	{
        "Id": 98,
        "Name": 'InputTicketsCount(int count)',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 74,
        "MainModuleId": None
    },
	{
        "Id": 99,
        "Name": 'InputSum(double money)',
        "CodeLinesNumber": 300,
        "ImportantIndex": 10,
        "RequirementId": 75,
        "MainModuleId": None
    },
	{
        "Id": 100,
        "Name": 'SetSafeModeManually()',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 76,
        "MainModuleId": None
    },
	{
        "Id": 101,
        "Name": 'SetSafeModeTimeDelay(Time time)',
        "CodeLinesNumber": 210,
        "ImportantIndex": 10,
        "RequirementId": 76,
        "MainModuleId": None
    },
	{
        "Id": 102,
        "Name": 'UnlockSafeMode()',
        "CodeLinesNumber": 400,
        "ImportantIndex": 10,
        "RequirementId": 76,
        "MainModuleId": None
    },
	{
        "Id": 103,
        "Name": 'InputPassword(string password)',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 76,
        "MainModuleId": None
    },
	{
        "Id": 104,
        "Name": 'CheckPassword()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 76,
        "MainModuleId": None
    },
	{
        "Id": 105,
        "Name": 'PrintScreenInfo()',
        "CodeLinesNumber": 140,
        "ImportantIndex": 10,
        "RequirementId": 77,
        "MainModuleId": None
    },
	{
        "Id": 106,
        "Name": 'DetermineStatus()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 77,
        "MainModuleId": None
    },
	{
        "Id": 107,
        "Name": 'GetDeviceContext(IntPtr handle)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 77,
        "MainModuleId": None
    },
	{
        "Id": 108,
        "Name": 'PrintScreenCharge(int charge)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 78,
        "MainModuleId": None
    },
	{
        "Id": 109,
        "Name": 'GetCharge()',
        "CodeLinesNumber": 175,
        "ImportantIndex": 10,
        "RequirementId": 78,
        "MainModuleId": None
    },
	{
        "Id": 110,
        "Name": 'CheckVoltage(double voltage)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 78,
        "MainModuleId": None
    },
	{
        "Id": 111,
        "Name": 'GetBatteryContext(IntPtr context)',
        "CodeLinesNumber": 350,
        "ImportantIndex": 10,
        "RequirementId": 78,
        "MainModuleId": None
    },
	{
        "Id": 112,
        "Name": 'PrintScreenCharging()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 79,
        "MainModuleId": None
    },
	{
        "Id": 113,
        "Name": 'GetChargingDeviceContext(IntPtr handle)',
        "CodeLinesNumber": 240,
        "ImportantIndex": 10,
        "RequirementId": 79,
        "MainModuleId": None
    },
	{
        "Id": 114,
        "Name": 'GetBatteryContext(IntPtr context)',
        "CodeLinesNumber": 350,
        "ImportantIndex": 10,
        "RequirementId": 79,
        "MainModuleId": None
    },
	{
        "Id": 115,
        "Name": 'CheckVoltage(double voltage)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 79,
        "MainModuleId": None
    },
	{
        "Id": 116,
        "Name": 'PrintScreenPaperOff()',
        "CodeLinesNumber": 140,
        "ImportantIndex": 10,
        "RequirementId": 80,
        "MainModuleId": None
    },
	{
        "Id": 117,
        "Name": 'GetPaperDeviceContext(IntPtr handle)',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 80,
        "MainModuleId": None
    },
	{
        "Id": 118,
        "Name": 'CheckPaper()',
        "CodeLinesNumber": 230,
        "ImportantIndex": 10,
        "RequirementId": 80,
        "MainModuleId": None
    },
	{
        "Id": 119,
        "Name": 'PrintScreenInkOff()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 81,
        "MainModuleId": None
    },
	{
        "Id": 120,
        "Name": 'GetInkDeviceContext(IntPtr handle)',
        "CodeLinesNumber": 280,
        "ImportantIndex": 10,
        "RequirementId": 81,
        "MainModuleId": None
    },
	{
        "Id": 121,
        "Name": 'CheckInk()',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 81,
        "MainModuleId": None
    },
	{
        "Id": 122,
        "Name": 'ChangeValues()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 82,
        "MainModuleId": None
    },
	{
        "Id": 123,
        "Name": 'SetTicketPrice(int price)',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 83,
        "MainModuleId": None
    },
	{
        "Id": 124,
        "Name": 'SetWarning(string message)',
        "CodeLinesNumber": 30,
        "ImportantIndex": 10,
        "RequirementId": 84,
        "MainModuleId": None
    },
	{
        "Id": 125,
        "Name": 'ApplyPower()',
        "CodeLinesNumber": 530,
        "ImportantIndex": 10,
        "RequirementId": 85,
        "MainModuleId": None
    },
	{
        "Id": 126,
        "Name": 'GetDeviceContext(IntPtr context)',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 85,
        "MainModuleId": None
    },
	{
        "Id": 127,
        "Name": 'On()',
        "CodeLinesNumber": 400,
        "ImportantIndex": 10,
        "RequirementId": 86,
        "MainModuleId": None
    },
	{
        "Id": 128,
        "Name": 'Off()',
        "CodeLinesNumber": 600,
        "ImportantIndex": 10,
        "RequirementId": 87,
        "MainModuleId": None
    },
	{
        "Id": 129,
        "Name": 'Reload()',
        "CodeLinesNumber": 620,
        "ImportantIndex": 10,
        "RequirementId": 88,
        "MainModuleId": None
    },
	{
        "Id": 130,
        "Name": 'StructureData()',
        "CodeLinesNumber": 190,
        "ImportantIndex": 10,
        "RequirementId": 89,
        "MainModuleId": None
    },
	{
        "Id": 131,
        "Name": 'DownloadData()',
        "CodeLinesNumber": 240,
        "ImportantIndex": 10,
        "RequirementId": 89,
        "MainModuleId": None
    },
	{
        "Id": 132,
        "Name": 'GetSum()',
        "CodeLinesNumber": 40,
        "ImportantIndex": 10,
        "RequirementId": 90,
        "MainModuleId": None
    },
	{
        "Id": 133,
        "Name": 'ComputeSum()',
        "CodeLinesNumber": 140,
        "ImportantIndex": 10,
        "RequirementId": 90,
        "MainModuleId": None
    },
	{
        "Id": 134,
        "Name": 'GetDatetime()',
        "CodeLinesNumber": 20,
        "ImportantIndex": 10,
        "RequirementId": 91,
        "MainModuleId": None
    },
	{
        "Id": 135,
        "Name": 'ProtectData()',
        "CodeLinesNumber": 700,
        "ImportantIndex": 10,
        "RequirementId": 92,
        "MainModuleId": None
    },
	{
        "Id": 136,
        "Name": 'InputPassword(string password)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 93,
        "MainModuleId": None
    },
	{
        "Id": 137,
        "Name": 'CheckPassword(string password)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 93,
        "MainModuleId": None
    },
	{
        "Id": 138,
        "Name": 'Crypt(string password)',
        "CodeLinesNumber": 140,
        "ImportantIndex": 10,
        "RequirementId": 93,
        "MainModuleId": None
    },
	{
        "Id": 139,
        "Name": 'Encrypt(string password)',
        "CodeLinesNumber": 140,
        "ImportantIndex": 10,
        "RequirementId": 93,
        "MainModuleId": None
    },
	{
        "Id": 140,
        "Name": 'ClearDatabase(string database)',
        "CodeLinesNumber": 60,
        "ImportantIndex": 10,
        "RequirementId": 93,
        "MainModuleId": None
    }
]
module_class = {
    "Id": int,
    "Name": str,
    "CodeLinesNumber": int,
    "ImportantIndex": int,
    "RequirementId": int,
    "MainModuleId": int
}

@app_module.route('/', methods=['GET'])
def get_module_set():
    return jsonify(module_set)

@app_module.route('/', methods=['POST'])
def create_module():
    if not request.json:
        abort(400)
    module = { 'Id': module_set[-1]['Id'] + 1 if len(module_set) else 1 }
    create_record(module_class, request, module)
    module_set.append(module)
    return jsonify(module), 201

@app_module.route('/<int:module_id>', methods = ['GET'])
def get_module(module_id):
    modules = list(filter(lambda t: t['Id'] == module_id, module_set))
    if len(modules) == 0:
        abort(404)
    return jsonify(modules[0])

@app_module.route('/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    modules = [module for module in module_set if module['Id'] == module_id]
    if len(modules) == 0 or not request.json:
        abort(404)
    module = modules[0]
    update_record(module_class, request, module)
    return jsonify(module)

@app_module.route('/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    modules = [module for module in module_set if module['Id'] == module_id]
    if len(modules) == 0:
        abort(404)
    module_set.remove(modules[0])
    return jsonify({'Result': True})
