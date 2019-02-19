<?php
  $API_KEY = '32c83590-8198-47f6-990d-c4396f3abd9a';
  $PAGE_ID = 'djp8vk59r4vq';
  $METRIC_ID = 'gc80d08g3ylx';
  $BASE_URI = 'https://api.statuspage.io/v1';
 
  $ch = curl_init(sprintf("%s/pages/%s/metrics/%s/data.json", $BASE_URI, $PAGE_ID, $METRIC_ID));
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "Authorization: OAuth " . $API_KEY,
      "Expect: 100-continue"
    )
  );
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 
  // need at least 1 data point for every 5 minutes
  // submit random data for the whole day
  $total_points = (60 / 5 * 24);
  for($i = 0; $i < $total_points; $i++) {
    $ts = time() - ($i * 5 * 60);
    $value = rand(0, 99);
    $postparams = array(
      "data[timestamp]" => $ts,
      "data[value]" => $value
    );
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postparams);
    curl_exec($ch);
 
    printf("Submitted point %d of %d\n", ($i + 1), $total_points);
    sleep(1);
  }
?>
