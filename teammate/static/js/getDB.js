	
				var raidBoss = {
					topicList : function(theGame, InstanceName){

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
		raidBoss.topics();
	})

		
	


		$(document).ready(function(){
			$('li ').click(function(){
			var keyword = $(this).text();
			var gameId = $(this).find('a').attr('no');
			$('.gameList a').html(keyword).attr('keyword',keyword);
			$('#theGame').attr('no',gameId);


			})



		$('.delete').click(function(){
			var ans = confirm("Are you sure you want to Delete this Record?");
			if(!ans){
				return false
			}
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




		});  
