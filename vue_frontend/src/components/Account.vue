<template>
	<div>
		<div id="form-layout-g">
			<div id="form-padding-g">
				<div id="form-container-g">
					<div id="account-profile" class="flex">
							<img v-bind:src="c_user_image" height="125" width="125">
							<div>
									<div> {{ user.username }} </div>
									<div> {{ user.email }} </div>
							</div>
					</div>
					<button v-if="user.display_picture!='default.png'" v-on:click="popup=true"> Remove Profile Picture </button>
					<h2> Update Account </h2>
					<label> Username </label>
					<input type="text" v-model="input.username">
					<div v-if="username_exist_error" class="error-input">Username already exist</div>
					<div v-else-if="username_char_error" class="error-input">Username must be between 3 and 25 characters long</div>
					<div v-else-if="user_space_error" class="error-input">Username must not contain spaces</div>
					<label> Email </label>
					<input type="text" v-model="input.email">
					<div v-if="email_invalid_error" class="error-input">Invalid email address</div>
					<label> Image Upload </label>
					<div v-if="image_invalid_error" class="error-input">File must have the extension .jpg or .png</div>
					<input type="file" name="image_file" ref="user_picture">
					<button v-on:click="update_details()" class="form-submit-g"> Update </button>
				</div>
			</div>
		</div>
		<div v-if="popup" id="popup-form-g">
			<div id="popup-wrapper-form-g">
				<div id="popup-container-form-g">
					<div> Remove User Account Image </div>
					<div> Are you sure you want to remove this image? </div>
					<div id="pop-up-buttons-form-g">
						<button v-on:click="remove_user_image()"> REMOVE </button>
						<button v-on:click="popup=false"> CANCEL </button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import {bus} from '../main.js';
import imageMixin from '../mixins/imageMixin';
import validationMixin from '../mixins/validationMixin';

export default {
	props: ['token', 'user'],
	data() {
		return {
			input: { username: this.user.username, email: this.user.email },
			username_exist_error: false,
			username_char_error: false,
			email_invalid_error: false,
			image_invalid_error: false,
			user_space_error: false,
			popup: false
		}
	},
  methods: {
		remove_user_image() {
			axios.delete(`${this.domain_name_api}remove_user_picture`, { headers: { 'x-access-token' : this.token } }).then(() => {
				this.user.display_picture = 'default.png';
				bus.$emit('show_hide_notify', 'User picture removed');
				this.popup = false;
			});
		},
    change_user_image() {
			let image = this.$refs['user_picture'].files[0];
			if(image) {
				let ext = image.name.split('.').pop(); // the extnesion will be the last period of the filename therefore pop is used
				if(ext != 'jpg' && ext != 'png') {
					this.image_invalid_error = true;
				} else {
					let form_data = new FormData();
					form_data.append("file", image);
					axios.post(`${this.domain_name_api}update_user_image`, form_data, { headers: { 'Content-Type': 'multipart/form-data', 'x-access-token' : this.token } }).then(response => {
						let picture = response.data.filename
						if(picture) {
							this.user.display_picture = picture;
						}
					})
				}
			}
		},
		update_details() {
			this.resetValidation();
			let username = this.input.username.trim();
      let email = this.input.email.trim();
			let validation_error = false;
			if(username.length < 3 || username.length > 25) {
        this.username_char_error = true;
        validation_error = true;
			} else if(!this.validUserSpace(username)) {
				this.user_space_error = true;
				validation_error = true;
			}
      if(!this.validEmail(email)) {
        this.email_invalid_error = true;
        validation_error = true;
			}
			if(!validation_error) {
				axios.put(`${this.domain_name_api}account`, {'username' : username, 'email' : email}, { headers: { 'x-access-token' : this.token } }).then(() => {
					this.change_user_image();
					this.user.username = username;
					this.user.email = email;
					bus.$emit('show_hide_notify', 'Account details updated');
				}).catch(err => {
          if(err.response.data.error) {
						this.username_exist_error = true;
          }
				});
			}
		},
		resetValidation() {
			this.username_exist_error = false;
			this.username_char_error = false;
			this.email_invalid_error = false;
			this.image_invalid_error = false;
			this.user_space_error = false;
		}
  },
	computed: {
    c_user_image() {
      return this.user_image(this.user.display_picture);
		}
	},
  created() {
		if(!this.token) {
			this.$router.push('/error403');
		}
	},
	mixins: [imageMixin, validationMixin]
};
</script>

<style scoped>
#form-layout-g {
  transform: translateY(25%);
}

#form-layout-g img {
	border-radius: 50%;
}

#account-profile > div {
	margin-left: 1.5rem;
}

#account-profile > div > div:nth-of-type(1) {
	font-size: 2.5rem;
	margin-bottom: 0.5rem;
}

#account-profile > div > div:nth-of-type(2) {
  font-size: 1.1rem;
}

#form-layout-g button:nth-of-type(1) {
	margin: 1rem 0;
}

@media (max-width: 992px) {
	#form-layout-g img {
    height: 100px;
    width: 100px;
  }

  #forum-profile > div {
    margin-left: 1.2rem;
  }

  #forum-profile > div > div:nth-of-type(1) {
    font-size: 2rem;
    margin-bottom: 0.3rem;
  }

  #forum-profile > div > div:nth-of-type(2) {
    font-size: 0.9rem;
  }
}

@media (max-width: 768px) {
	
}
</style>
