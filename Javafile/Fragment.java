
//FRAGMENT REPLACEMENT
private void replaceFragment(Fragment fragment){
FragmentManager fragment = getSupportFragmentManager();
FragmentTransaction transaction = fragment.beginTransaction();
transaction.replace(R.id.frameLayout,fragment);
transaction.commit()
}



//Intents are used to communicate between different components of an application or between different applications

 There are two main types of intents:

 1. Explicit Intent  : Use explicit intents when you need to start a specific component within your application.

Intent explicitIntent = new Intent(this, TargetActivity.class);
startActivity(explicitIntent);



2. Implicit Intent
Definition: An implicit intent does not specify the component to be started. Instead, it declares an action to be performed, and the Android system determines which component can handle the action.
Usage: It is used when you want to perform a generic action that can be handled by any component that supports the specified action.
Example:


Use implicit intents when you want to perform a generic action that can be handled by any component in the system.

Intent implicitIntent = new Intent(Intent.ACTION_SEND);
implicitIntent.setType("text/plain");
implicitIntent.putExtra(Intent.EXTRA_TEXT, "Hello, this is a test message.");
startActivity(implicitIntent);


Intent intent = new Intent(Intent.ACTION_SEND);
intent.setType("text/plain");
intent.setPackage("com.whatsapp"); // Specify the package name of WhatsApp
intent.putExtra(Intent.EXTRA_TEXT, "Hello, this is a message from my app.");
startActivity(intent);



Uri uri = Uri.parse("https://www.example.com");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);
Toast.makeText(this, "No application can handle opening this URL", Toast.LENGTH_SHORT).show();