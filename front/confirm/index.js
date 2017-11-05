
import Confirm from './confirm';
import events from './eventbus';


/* eslint-disable no-param-reassign */
const confirma = {
  install(Vue) {
    if (this.installed) {
      return;
    }

    this.installed = true;

    Vue.component('confirm', Confirm);
    Vue.prototype.$confirm = (params) => {

      events.$emit('vconfirm-open', params);
      events.$on('vconfirm-close', (flag) => {
            if(flag)
            {
              console.log('plugin',params.upload._id);
              params.execute(params.upload);
              events.$off('vconfirm-close');
            }
      });
    };
  },
};

export default confirma;
