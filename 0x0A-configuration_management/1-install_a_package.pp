# Puppet manifest to install Flask version 2.1.0 using pip3
# This manifest installs Flask version 2.1.0 using pip3 package manager

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
