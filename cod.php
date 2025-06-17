// Получение сотрудников
$query = db_query("
    SELECT field_2439, field_2438 
    FROM app_entity_104 
    WHERE field_10768 = '6987' 
      AND field_7470 IN ('6753', '6754', '6392');
");

if (!$query) {
    die('Ошибка запроса (workers): ' . db_error());
}

$names = [];       // ФИО => "Имя Фамилия"
$workers__ = [];   // для быстрого поиска по ФИО

while ($row = db_fetch_array($query)) {
    $full_name = trim($row['field_2439']) . ' ' . trim($row['field_2438']);
    $names[$full_name] = $full_name;
    $workers__[$full_name] = true;
}

// Инициализация счётчиков
$__actually_first_order = array_fill_keys(array_keys($names), 0);
$__actually = array_fill_keys(array_keys($names), 0);
$__re_potencial = array_fill_keys(array_keys($names), 0);
$__potencial = array_fill_keys(array_keys($names), 0);

// Получение заказов
$query = db_query("
    SELECT field_10062, field_3617
    FROM app_entity_68
    WHERE field_3676 = '5205' AND field_10062 IN ('7267', '6883', '6884', '6885');
");

if (!$query) {
    die('Ошибка запроса (orders): ' . db_error());
}

while ($row = db_fetch_array($query)) {
    $value = $row['field_10062'];
    $worker_name = trim($row['field_3617']); // ФИО

    if (isset($workers__[$worker_name])) {
        if ($value == '7267') {
            $__actually_first_order[$worker_name]++;
        } elseif ($value == '6883') {
            $__actually[$worker_name]++;
        } elseif ($value == '6884') {
            $__re_potencial[$worker_name]++;
        } elseif ($value == '6885') {
            $__potencial[$worker_name]++;
        }
    }
}

// Вычисление общих итогов
$total_first = array_sum($__actually_first_order);
$total_actually = array_sum($__actually);
$total_repot = array_sum($__re_potencial);
$total_pot = array_sum($__potencial);

// Вывод результатов
echo "<pre>";
printf("%-25s | %6s | %6s | %6s | %6s\n", "Сотрудник", "1-й", "Акт", "Повт", "Потенц");
echo str_repeat("-", 60) . "\n";
printf("%-25s | %6d | %6d | %6d | %6d\n", "ИТОГО", $total_first, $total_actually, $total_repot, $total_pot);
echo str_repeat("-", 60) . "\n";

foreach ($names as $full_name) {
    printf(
        "%-25s | %6d | %6d | %6d | %6d\n",
        $full_name,
        $__actually_first_order[$full_name],
        $__actually[$full_name],
        $__re_potencial[$full_name],
        $__potencial[$full_name]
    );
}
echo "</pre>";
