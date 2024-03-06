# Puppet manifest to fix Apache 500 error

exec { 'fix_apache_error':
  command     => 'service apache2 restart',
  path        => '/usr/bin',
  onlyif      => 'curl -sI 127.0.0.1 | grep "500 Internal Server Error"',
  require     => Package['apache2'],
}

service { 'apache2':
  ensure  => running,
  enable  => true,
}

