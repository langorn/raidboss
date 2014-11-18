	
var attitudeList = [];

				var raidBoss = {
					topicList : function(theGame, InstanceName){
						console.log(theGame+'...'+InstanceName);
						$('#gameCollection').html('');
						$.getJSON('/topic/search/'+theGame+'/'+InstanceName+'/',function(data){
							
							console.log(data);
							$('#raidBossTB tbody').html('');
							var tdata = '';
							for(d in data){
								tdata += '<tr><td><i class="Shield icon ui"></i>Wildstar</td><td><a href="/topic/'+data[d].pk+'">'+data[d].fields.title+'</a></td>';
								tdata+='<td>'+data[d].fields.create_date+'</td>';
								tdata+='<td>'+data[d].fields.quantity+'</td>';
								tdata+='</tr>';
							}		
							$('#raidBossTB tbody').html(tdata);


						})
						.error(function(jqXHR, textStatus, errorThrown) {
					        console.log("error " + textStatus);
					        console.log("incoming Text " + jqXHR.responseText);
		    			})
					},
					byInstance : function(theGame, InstanceId){
						console.log(theGame+'...'+InstanceId);
						$('#gameCollection').html('');
						$.getJSON('/topic/by_instance/'+theGame+'/'+InstanceId+'/',function(data){
							
							console.log(data);
							$('#raidBossTB tbody').html('');
							var tdata = '';
							for(d in data){
								tdata += '<tr><td><i class="Shield icon ui"></i>Wildstar</td><td><a href="/topic/'+data[d].pk+'">'+data[d].fields.title+'</a></td>';
								tdata+='<td>'+data[d].fields.create_date+'</td>';
								tdata+='<td>'+data[d].fields.quantity+'</td>';
								tdata+='</tr>';
							}		
							$('#raidBossTB tbody').html(tdata);
							$('#raidBossTB').show();


						})
						.error(function(jqXHR, textStatus, errorThrown) {
					        console.log("error " + textStatus);
					        console.log("incoming Text " + jqXHR.responseText);
		    			})
					},
					topics: function(){


						$.getJSON('/topics',function(data){
							console.log(data);

							$('#raidBossTB tbody').html('');
							var tdata = '';
							for(d in data){
								tdata += '<tr><td><i class="Shield icon ui"></i>Wildstar</td><td><a href="/topic/'+data[d].pk+'">'+data[d].fields.title+'</a></td>';
								tdata+='<td>'+data[d].fields.create_date+'</td>';
								tdata+='<td>'+data[d].fields.quantity+'</td>';
								tdata+='</tr>';
							}		


							$('#raidBossTB tbody').html(tdata);

						})
						.error(function(jqXHR, textStatus, errorThrown) {
					        console.log("error " + textStatus);
					        console.log("incoming Text " + jqXHR.responseText);
		    			})
					},
					listGame: function(){

						$.getJSON('/listGame',function(data){
							var items = [];

							for(var k in data){
								var game = {};
								game['name']= data[k].fields.name;
								game['description'] = data[k].fields.description;
								game['type'] = data[k].fields.type;
								game['id'] = data[k].pk;
								game['photo_id'] = data[k].pk;
								game['level'] = 0;
								game['inst'] = 0;
								game['post_count'] = data[k].fields.post_count;
								items.push(game);
							}
							console.log(items);
							// var template = $('#gameImages').html();
							// $("#gameCollection").html(_.template(template,{'items':items}));
							var template = _.template(($('#gameImages').html()))
							var resultinghtml = template({items:items})
							$("#gameCollection").html(resultinghtml);

						})
						.error(function(jqXHR, textStatus, errorThrown) {
					        console.log("error " + textStatus);
					        console.log("incoming Text " + jqXHR.responseText);
		    			})
					},
					listDungeon:function(gameId){

						$.getJSON('/listDungeon/'+gameId+'/',function(data){
							var items = [];

							for(var k in data){
								console.log(data[k]);
								var game = {};
								game['name']= data[k].fields.name;
								game['description'] = data[k].fields.description;
								game['type'] = data[k].fields.type;
								game['id'] = gameId;
								game['photo_id'] = 'd'+data[k].pk;
								game['level'] = 1;
								game['inst'] = data[k].pk;
								game['post_count'] = data[k].fields.post_count;
								items.push(game);
							}

							// var template = $('#gameImages').html();
							// $("#gameCollection").html(_.template(template,{'items':items}));
							var template = _.template(($('#gameImages').html()))
							var resultinghtml = template({items:items})
							$("#gameCollection").html(resultinghtml);

						})
						.error(function(jqXHR, textStatus, errorThrown) {
					        console.log("error " + textStatus);
					        console.log("incoming Text " + jqXHR.responseText);
		    			})

					}
				}



		
			var bestPictures = new Bloodhound({
			  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('values'),
			  queryTokenizer: Bloodhound.tokenizers.whitespace,
			  remote: {
				    url: '/ajax_search/%QUERY',
				    filter: function(list) {
				    	
				      return $.map(list, function(country) { //console.log(country); 
				      	return { name: country.fields.name, pk:country.pk }; });
				    }
			   }	   
			  });
			 
			bestPictures.initialize();
			 
			$('#remote .typeahead').typeahead(
				{
					highlight:true
				},
				{
			  	name: 'pk',
			 	displayKey: 'name',
			 	valueKey:'pk',
			    source: bestPictures.ttAdapter(),
			    template: [ '<p class="name">{{pk}}</p>',
			    '<p class="lang">{{pk}}</p>'].join('')	})

				.bind("typeahead:selected", function(obj, datum, name) {
					
					if(!datum){
						return
					}
						var id = datum.pk
					//window.location.href = '/crm/student/'+datum.pk;
					var theGame = $('#theGame').attr('no');
					var InstanceName = datum.name;
					raidBoss.topicList(theGame, InstanceName)
					console.log( datum, name);
				});

				$('.delete').click(function(){
					var ans = confirm("Are you sure you want to Delete this Record?");
					if(!ans){
						return false
					}
				})

		//load all 
	$(function(){
		raidBoss.listGame();
	})

		
	


		$(document).ready(function(){

				 /* FB */
				 // This is called with the results from from FB.getLoginStatus().
				  function statusChangeCallback(response) {
				    console.log('statusChangeCallback');
				    console.log(response);
				    // The response object is returned with a status field that lets the
				    // app know the current login status of the person.
				    // Full docs on the response object can be found in the documentation
				    // for FB.getLoginStatus().
				    if (response.status === 'connected') {
				      // Logged into your app and Facebook.
				      testAPI();
				    } else if (response.status === 'not_authorized') {
				      // The person is logged into Facebook, but not your app.
				      document.getElementById('status').innerHTML = 'Please log ' +
				        'into this app.';
				    } else {
				      // The person is not logged into Facebook, so we're not sure if
				      // they are logged into this app or not.
				      document.getElementById('status').innerHTML = 'Please log ' +
				        'into Facebook.';
				    }
				  }

				  // This function is called when someone finishes with the Login
				  // Button.  See the onlogin handler attached to it in the sample
				  // code below.
				  function checkLoginState() {
				    FB.getLoginStatus(function(response) {
				      statusChangeCallback(response);
				    });
				  }

				  window.fbAsyncInit = function() {
				  FB.init({
				    appId      : '1539034969661881',
				    cookie     : true,  // enable cookies to allow the server to access 
				                        // the session
				    xfbml      : true,  // parse social plugins on this page
				    version    : 'v2.1' // use version 2.1
				  });

				  // Now that we've initialized the JavaScript SDK, we call 
				  // FB.getLoginStatus().  This function gets the state of the
				  // person visiting this page and can return one of three states to
				  // the callback you provide.  They can be:
				  //
				  // 1. Logged into your app ('connected')
				  // 2. Logged into Facebook, but not your app ('not_authorized')
				  // 3. Not logged into Facebook and can't tell if they are logged into
				  //    your app or not.
				  //
				  // These three cases are handled in the callback function.

				  FB.getLoginStatus(function(response) {
				    statusChangeCallback(response);
				  });

				  };

				  // Load the SDK asynchronously
				  (function(d, s, id) {
				    var js, fjs = d.getElementsByTagName(s)[0];
				    if (d.getElementById(id)) return;
				    js = d.createElement(s); js.id = id;
				    js.src = "//connect.facebook.net/en_US/sdk.js";
				    fjs.parentNode.insertBefore(js, fjs);
				  }(document, 'script', 'facebook-jssdk'));

				  // Here we run a very simple test of the Graph API after login is
				  // successful.  See statusChangeCallback() for when this call is made.
				  function testAPI() {
				    console.log('Welcome!  Fetching your information.... ');
				    FB.api('/me', function(response) {

				      console.log('Successful login for: ' + response.name);
				        
				      try{
				        document.getElementById('status').innerHTML ='Thanks for logging in, ' + response.name + '!';
				      }catch(err){}
				        
				        findUserByDB(response.id, response.name, response.email,response.gender);

				    });
				  }

				    function findUserByDB(id,name,email,gender){
				      $.getJSON('/findUserByDB', 
				                { facebook_id: id, name: name , email:email, gender:gender },
				                function() {
				                  //console.log(data);
				                  location.reload(true);
				                });
				      };






				$('li ').click(function(){
				var keyword = $(this).text();
				var gameId = $(this).find('a').attr('no');
				$('.gameList a').eq(0).html(keyword).attr('keyword',keyword);
				$('#theGame').attr('no',gameId);
				})

			$('.delete').click(function(){
				var ans = confirm("Are you sure you want to Delete this Record?");
				if(!ans){
					return false
				}
			})

			$('#gameCollection').on('click','.item',function(){
				
				var gameId = $(this).attr('gameId');
				var level = $(this).attr('level');
				var inst = $(this).attr('instId');
				// alert(level);
				if(level==0){
					// $('#gameCollection .item').attr('level',1);
					
				}else{
					// alert(level);
					raidBoss.byInstance(gameId,inst);
					return
				}
				$("#gameCollection").html('');
				raidBoss.listDungeon(gameId);
				$("#gameCollection").prev('div').html('<button class="ui button">BACK</button>');

			})

			$('#back').click(function(){

				// $(this).hide();
				$('#raidBossTB').hide();
				raidBoss.listGame();
			})


			$('#id_game_name').change(function(){
				var game_id = $(this).val()
				$.getJSON('/getInstance/'+game_id,function(data){
						var options = '';
						for(var k in data){
							options += '<option value="'+data[k].pk+'">'+data[k].fields.name+'</option>'
						}
						$('#Instance').html(options)
						//
				})


				$.getJSON('/getAttrs/'+game_id,function(data){
						var options = '';
						for(var k in data){
							options += '<option value="'+data[k].pk+'">'+data[k].fields.name+'</option>'
						}
						$('#requirement').html(options)
				})

			})

			$('#Instance').change(function(){
				var instance = $(this).val();
				$('input[name="Instance"]').val(instance);

			})

			$('#logout').click(function(){

				if(FB.getAuthResponse()){
					FB.logout(function(response) {
				        // Person is now logged out
				        window.location.href="/logout";
				        return
				    });

				}
				window.location.href="/logout";
			})
		});  


		    function getCookie(name) {
		        var cookieValue = null;
		        if (document.cookie && document.cookie != '') {
		            var cookies = document.cookie.split(';');
		            for (var i = 0; i < cookies.length; i++) {
		                var cookie = jQuery.trim(cookies[i]);
		                // Does this cookie string begin with the name we want?
		                if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                    break;
		                }
		            }
		        }
		        return cookieValue;
		    }
		    var csrftoken = getCookie('csrftoken');



