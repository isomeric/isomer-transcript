/*!
 * Isomer - The distributed application framework
 * ==============================================
 * Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

'use strict';

/**
 * @ngdoc function
 * @name isomerFrontendApp.controller:TranscriptCtrl
 * @description
 * # TranscriptCtrl
 * Controller of the isomerFrontendApp
 */
class Transcript {

    constructor(scope, rootscope, $modal, navdata, user, objectproxy, socket, menu) {
        this.scope = scope;
        this.rootscope = rootscope;
        this.$modal = $modal;
        this.navdata = navdata;
        this.user = user;
        this.op = objectproxy;
        this.socket = socket;
        this.menu = menu;

        this.beverages = {};
        this.fieldnames = ['name', 'fullname', 'location', 'text', 'image'];

        let self = this;

        this.request_beverages = function () {
            console.log('[TRANSCRIPT] Login successful - fetching user data');
            this.op.search('user', '*', ['name', 'description']).then(function (msg) {
                let users = msg.data.list;
                console.log("[TRANSCRIPT] Users: ", users);
                for (let user of users) {
                    let user_entry = {
                        name: user.name,
                        uuid: user.uuid,
                        dropdown: false
                    };
                    self.op.search('profile', {owner: user.uuid}, '*').then(function (msg) {
                        // TODO: Why is this a search? Should probably be a 'get'.
                        let profile = msg.data.list[0];
                        console.log('[TRANSCRIPT] Profile:', profile);
                        if (typeof profile !== 'undefined') {
                            user_entry.fullname = profile.userdata.name + ' ' + profile.userdata.familyname;
                            user_entry.location = profile.userdata.location;
                            user_entry.text = profile.userdata.notes;
                            user_entry.image = profile.userdata.image;
                        } else {
                            user_entry.text = 'No profile';
                        }
                    });
                    self.beverages[user.uuid] = user_entry;
                }
            });
        };

        self.socket.listen('isomer.auth.login', self.handleNavdata);

        this.loginupdate = this.rootscope.$on('User.Login', function () {
            self.request_beverages();
        });

        if (this.user.signedin === true) {
            self.request_beverages();
        }


        self.scope.$on('$destroy', function () {
        });
    }
}

Transcript.$inject = ['$scope', '$rootScope', '$modal', 'navdata', 'user', 'objectproxy', 'socket', 'menu'];

export default Transcript;