# Puppet manifest to kill a process named killmenow
# This manifest uses the exec resource to execute the pkill command to terminate the process

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
