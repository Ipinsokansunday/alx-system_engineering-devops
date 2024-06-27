# Ensure puppetlabs-stdlib is available
if !('puppetlabs-stdlib' in $::modules) {
  package { 'puppetlabs-stdlib':
    ensure => present,
  }
}

file_line { 'increase-hard-file-limit-holberton-user':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 50000',
  match => '^holberton hard nofile',
}

file_line { 'increase-soft-file-limit-for-holberton-user':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 50000',
  match => '^holberton soft nofile',
}
