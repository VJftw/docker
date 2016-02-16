require 'docker'

repository = 'vjftw'

desc 'Build Image by given relative Directory and push'
task :build, :dir do |t, args|
  dir = args[:dir]
  Dir.chdir dir
  tag = "#{repository}/#{dir.delete '_'}"
  puts "# Building #{tag}\n"

  image = Docker::Image.build_from_dir(Dir.getwd, {
      'dockerfile' => "Dockerfile",
      't' => tag
  }) do |v|
    if (log = JSON.parse(v)) && log.has_key?('stream')
      $stdout.puts log['stream']
    end
  end

  puts "\n# Pushing to Registry"

  docker_email = ENV['DOCKER_EMAIL']
  docker_username = ENV['DOCKER_USERNAME']
  docker_password = ENV['DOCKER_PASSWORD']
  Docker.authenticate!({
     'username' => docker_username,
     'password' => docker_password,
     'email' => docker_email
  })

  image.push do |chunk|
    puts JSON.parse(chunk)
  end
end
