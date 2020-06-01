function Node(data){
    this.data=data;
    this.next=null;
}

function Solution(){

	this.insert=function(head,data){
          //complete this method
        let node = new Node(data);
        if (head === null){
			head = node;
		} else {
			head.next = node;	
			console.log(head.next);
		}
        return head;
    };

	this.display=function(head){
        var start=head;
            while(start){
                process.stdout.write(start.data+" ");
                start=start.next;
            }
    };
}

var T=4;
var head=null;
var mylist=new Solution();
var numbers = [2, 3, 4, 1];
for(i=0;i<T;i++){
	var data=parseInt(numbers[i]);
	head=mylist.insert(head,data);
	console.log('Head:', head);
}
mylist.display(head);
